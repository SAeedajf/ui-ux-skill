#!/usr/bin/env python3
"""Exercise the MCP HTTP contract and security middleware against local PHP."""

from __future__ import annotations

import json
import os
from pathlib import Path
import argparse
import socket
import subprocess
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "mcp-server"
TOKEN = "local-test-token-for-integration"


def request(url: str, payload: dict | None = None, *, session: str | None = None,
            token: str | None = TOKEN, origin: str | None = None, host: str | None = None):
    headers = {"Accept": "application/json, text/event-stream"}
    if payload is not None:
        headers["Content-Type"] = "application/json"
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    if session:
        headers["Mcp-Session-Id"] = session
    if origin:
        headers["Origin"] = origin
    if host:
        headers["Host"] = host
    req = Request(url, data=None if payload is None else json.dumps(payload).encode(), headers=headers)
    with urlopen(req, timeout=3) as response:
        return response.status, dict(response.headers), response.read().decode()


def expect_http_error(url: str, expected: int, **kwargs) -> None:
    try:
        request(url, {"jsonrpc": "2.0", "id": 99, "method": "tools/list", "params": {}}, **kwargs)
    except HTTPError as error:
        if error.code != expected:
            raise AssertionError(f"Expected HTTP {expected}, got {error.code}") from error
        return
    raise AssertionError(f"Expected HTTP {expected}, got success")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app-root", type=Path, default=Path(os.environ.get("UIUX_MCP_APP_ROOT", APP)))
    parser.add_argument("--skills-dir", type=Path, default=Path(os.environ.get("UIUX_MCP_SKILLS_DIR", ROOT / ".agents" / "skills")))
    args = parser.parse_args()
    app_root = args.app_root.resolve()
    skills_dir = args.skills_dir.resolve()
    if not (app_root / "public" / "index.php").is_file() or not skills_dir.is_dir():
        raise SystemExit("The selected MCP app root or Skills directory is incomplete.")
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    base = f"http://127.0.0.1:{port}/"
    with tempfile.TemporaryDirectory(prefix="uiux-mcp-test-") as session_dir:
        env = os.environ.copy()
        env.update({
            "UIUX_MCP_BEARER_TOKEN": TOKEN,
            "UIUX_MCP_ALLOWED_HOSTS": "127.0.0.1,localhost",
            "UIUX_MCP_SKILLS_DIR": str(skills_dir),
            "UIUX_MCP_SESSION_DIR": session_dir,
        })
        process = subprocess.Popen(
            ["php", "-S", f"127.0.0.1:{port}", "-t", str(app_root / "public")],
            cwd=app_root, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        try:
            for _ in range(40):
                if process.poll() is not None:
                    raise AssertionError("PHP development server exited before becoming ready")
                try:
                    status, _, health = request(base + "health.php", token=None)
                    if status == 200 and '"status":"ok"' in health:
                        break
                except (URLError, TimeoutError):
                    time.sleep(0.1)
            else:
                raise AssertionError("MCP HTTP service did not become ready")

            status, _, legacy_health = request(base + "health", token=None)
            assert status == 200 and '"status":"ok"' in legacy_health

            initialize_payload = {
                "jsonrpc": "2.0", "id": 1, "method": "initialize",
                "params": {"protocolVersion": "2025-11-25", "capabilities": {},
                           "clientInfo": {"name": "integration-test", "version": "1"}},
            }
            status, _, root_initialized = request(base, initialize_payload)
            assert status == 200 and '"protocolVersion":"2025-11-25"' in root_initialized

            endpoint = base + "index.php"
            status, headers, initialized = request(endpoint, initialize_payload)
            session = headers.get("Mcp-Session-Id") or headers.get("mcp-session-id")
            assert status == 200 and session and '"protocolVersion":"2025-11-25"' in initialized

            calls = [
                ("tools/list", {}, "list_uiux_skills"),
                ("tools/call", {"name": "list_uiux_skills", "arguments": {}}, "visual-hierarchy"),
                ("tools/call", {"name": "read_uiux_skill", "arguments": {"skill_id": "forms-input"}}, "name: forms-input"),
                ("tools/call", {"name": "read_uiux_reference", "arguments": {"skill_id": "forms-input", "path": "references/form-review.md"}}, "# Form review"),
                ("resources/list", {}, "forms-input"),
                ("resources/read", {"uri": "uiux://skills/forms-input"}, "name: forms-input"),
            ]
            for index, (method, params, expected) in enumerate(calls, 2):
                status, _, result = request(endpoint, {"jsonrpc": "2.0", "id": index, "method": method, "params": params}, session=session)
                assert status == 200 and expected in result, (method, result[:300])
            expect_http_error(endpoint, 401, token=None)
            expect_http_error(endpoint, 403, origin="https://untrusted.example")
            expect_http_error(endpoint, 403, host="untrusted.example")
            print("PASS: root and explicit PHP routes, 15-Skill tools, Skill/reference reads, resources, and auth/origin/host rejection")
            return 0
        finally:
            process.terminate()
            process.wait(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())
