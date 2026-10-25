#!/usr/bin/env python3
"""Read-only authenticated acceptance check for the hosted UI/UX Pro MCP server."""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import socket
import ssl
import sys
from typing import Callable
from urllib.parse import urlsplit


PROTOCOL_VERSION = "2025-11-25"
MAX_RESPONSE_BYTES = 2 * 1024 * 1024
REQUIRED_TOOLS = {
    "list_uiux_skills",
    "search_uiux_guidance",
    "read_uiux_skill",
    "read_uiux_reference",
}


class AcceptanceError(RuntimeError):
    """Raised when the endpoint does not satisfy the remote acceptance contract."""


def parse_endpoint(value: str) -> tuple[str, int, str]:
    parsed = urlsplit(value)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Endpoint must be an HTTPS URL without credentials.")
    if parsed.query or parsed.fragment:
        raise ValueError("Endpoint must not include a query string or fragment.")
    try:
        port = parsed.port or 443
    except ValueError as error:
        raise ValueError("Endpoint must use a valid port.") from error
    path = parsed.path or "/"
    if not path.startswith("/") or any(ord(character) < 32 for character in path):
        raise ValueError("Endpoint path must be absolute and contain no control characters.")
    return parsed.hostname, port, path


def decode_jsonrpc_response(content_type: str, body: bytes, request_id: int) -> dict:
    if len(body) > MAX_RESPONSE_BYTES:
        raise AcceptanceError("Response exceeded the 2 MiB safety limit.")
    media_type = content_type.split(";", 1)[0].strip().lower()
    try:
        if media_type == "application/json":
            messages = [json.loads(body)]
        elif media_type == "text/event-stream":
            text = body.decode("utf-8")
            messages = []
            for event in re.split(r"\r?\n\r?\n", text):
                data = "\n".join(
                    line[5:].lstrip(" ") for line in event.splitlines() if line.startswith("data:")
                )
                if data:
                    messages.append(json.loads(data))
        else:
            raise AcceptanceError(f"Unsupported MCP response content type: {media_type or 'missing'}.")
    except (UnicodeDecodeError, json.JSONDecodeError, TypeError) as error:
        raise AcceptanceError("MCP endpoint returned malformed JSON/JSON-RPC data.") from error

    if not isinstance(messages, list):
        raise AcceptanceError("MCP endpoint returned an invalid response envelope.")
    for message in messages:
        if isinstance(message, dict) and message.get("id") == request_id:
            if message.get("jsonrpc") != "2.0":
                raise AcceptanceError("MCP endpoint returned a non-JSON-RPC 2.0 response.")
            if "error" in message:
                error = message["error"]
                detail = error.get("message", "unknown JSON-RPC error") if isinstance(error, dict) else "invalid JSON-RPC error"
                raise AcceptanceError(f"MCP request failed: {detail}")
            result = message.get("result")
            if not isinstance(result, dict):
                raise AcceptanceError("MCP endpoint returned a missing or invalid result object.")
            return result
    raise AcceptanceError(f"MCP endpoint did not return a response for request id {request_id}.")


class HttpsPostTransport:
    """Minimal HTTPS transport that verifies TLS and never follows redirects."""

    def __init__(self, endpoint: str, token: str, timeout: float = 10.0):
        self.host, self.port, self.path = parse_endpoint(endpoint)
        if not re.fullmatch(r"[A-Za-z0-9._~+/-]+=*", token):
            raise ValueError("Bearer token contains characters unsupported by the server's authentication contract.")
        self.token = token
        self.timeout = timeout

    def __call__(self, payload: dict, *, authenticated: bool, session_id: str | None = None):
        headers = {
            "Accept": "application/json, text/event-stream",
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "MCP-Protocol-Version": PROTOCOL_VERSION,
        }
        if authenticated:
            headers["Authorization"] = f"Bearer {self.token}"
        if session_id:
            headers["Mcp-Session-Id"] = session_id

        connection = http.client.HTTPSConnection(
            self.host, self.port, timeout=self.timeout, context=ssl.create_default_context()
        )
        try:
            connection.request("POST", self.path, body=json.dumps(payload).encode("utf-8"), headers=headers)
            response = connection.getresponse()
            body = response.read(MAX_RESPONSE_BYTES + 1)
            return response.status, {key.lower(): value for key, value in response.getheaders()}, body
        except (OSError, ssl.SSLError, http.client.HTTPException, socket.timeout) as error:
            raise AcceptanceError(f"HTTPS request failed ({type(error).__name__}).") from error
        finally:
            connection.close()


def _header(headers: dict, name: str) -> str | None:
    target = name.lower()
    return next((value for key, value in headers.items() if key.lower() == target), None)


def _json_result(response: tuple[int, dict, bytes], request_id: int, stage: str) -> dict:
    status, headers, body = response
    if status in (301, 302, 303, 307, 308):
        raise AcceptanceError(f"{stage} failed: HTTP redirect refused; token is never forwarded to another URL.")
    if status != 200:
        raise AcceptanceError(f"{stage} failed: HTTP {status}.")
    return decode_jsonrpc_response(_header(headers, "content-type") or "", body, request_id)


def run_acceptance(endpoint: str, post: Callable):
    """Check auth rejection, MCP initialization, tool inventory, and a real Skill read."""
    initialize = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {},
            "clientInfo": {"name": "ui-ux-pro-acceptance-check", "version": "1.0.0"},
        },
    }
    unauthorized = dict(initialize, id=0)
    status, _, _ = post(unauthorized, authenticated=False)
    if status != 401:
        raise AcceptanceError(f"Unauthenticated initialize was not rejected with HTTP 401 (got {status}).")

    status, headers, body = post(initialize, authenticated=True)
    init_result = _json_result((status, headers, body), 1, "initialize")
    if init_result.get("protocolVersion") != PROTOCOL_VERSION:
        raise AcceptanceError("Server negotiated an unexpected MCP protocol version.")
    server_info = init_result.get("serverInfo")
    if not isinstance(server_info, dict) or not isinstance(server_info.get("name"), str):
        raise AcceptanceError("MCP initialize response did not identify the server.")
    session_id = _header(headers, "mcp-session-id")

    initialized = {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}
    status, _, _ = post(initialized, authenticated=True, session_id=session_id)
    if status != 202:
        raise AcceptanceError(f"initialized notification failed: expected HTTP 202, got {status}.")

    tools_payload = {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}
    tools_result = _json_result(post(tools_payload, authenticated=True, session_id=session_id), 2, "tools/list")
    tools = tools_result.get("tools")
    if not isinstance(tools, list):
        raise AcceptanceError("tools/list did not return a tools array.")
    tool_names = {item.get("name") for item in tools if isinstance(item, dict)}
    missing = sorted(REQUIRED_TOOLS - tool_names)
    if missing:
        raise AcceptanceError(f"tools/list is missing required tools: {', '.join(missing)}.")

    read_payload = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {"name": "read_uiux_skill", "arguments": {"skill_id": "forms-input"}},
    }
    read_result = _json_result(post(read_payload, authenticated=True, session_id=session_id), 3, "read_uiux_skill")
    if read_result.get("isError") is True:
        raise AcceptanceError("read_uiux_skill returned an MCP tool error.")
    content = read_result.get("content")
    text_content = "\n".join(
        item.get("text", "") for item in content if isinstance(item, dict) and item.get("type") == "text"
    ) if isinstance(content, list) else ""
    if "name: forms-input" not in text_content:
        raise AcceptanceError("read_uiux_skill did not return the expected forms-input Skill content.")

    return {
        "endpoint": endpoint,
        "server_name": server_info["name"],
        "server_version": server_info.get("version", "unknown"),
        "protocol_version": PROTOCOL_VERSION,
        "tool_count": len(tools),
        "skill_read": "forms-input",
        "authentication_required": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify authenticated remote MCP initialize, tools/list, and a read-only Skill fetch."
    )
    parser.add_argument("endpoint", help="HTTPS MCP endpoint, e.g. https://mcp.example.com/index.php")
    parser.add_argument("--token-env", default="UIUX_MCP_BEARER_TOKEN", help="Environment variable holding the bearer token")
    parser.add_argument("--timeout", type=float, default=10.0, help="HTTPS request timeout in seconds (default: 10)")
    args = parser.parse_args()
    if not 1 <= args.timeout <= 30:
        parser.error("--timeout must be between 1 and 30 seconds")
    token = os.environ.get(args.token_env, "")
    if not token:
        parser.error(f"Set {args.token_env} in the environment; do not pass tokens on the command line.")
    try:
        transport = HttpsPostTransport(args.endpoint, token, args.timeout)
        result = run_acceptance(args.endpoint, transport)
    except (ValueError, AcceptanceError) as error:
        print(f"MCP remote acceptance: BLOCKED ({error})")
        return 1

    print("Unauthenticated access: PASS (HTTP 401)")
    print(f"Initialize: PASS ({result['server_name']} {result['server_version']}; {result['protocol_version']})")
    print(f"tools/list: PASS ({result['tool_count']} tools; all expected tools present)")
    print(f"Skill read: PASS ({result['skill_read']}; response content verified)")
    print("MCP remote acceptance: PASS (read-only authenticated path)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
