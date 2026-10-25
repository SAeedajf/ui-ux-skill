"""Regression tests for the read-only remote MCP acceptance check."""

import json
import argparse
import unittest
from unittest.mock import patch

from scripts.mcp_remote_acceptance import (
    AcceptanceError,
    HttpsPostTransport,
    decode_jsonrpc_response,
    parse_endpoint,
    run_acceptance,
)
from scripts.check_mcp_endpoint import parse_endpoint as parse_preflight_endpoint


class RemoteMcpAcceptanceTests(unittest.TestCase):
    def test_endpoint_requires_https_without_credentials_query_or_fragment(self):
        self.assertEqual(
            ("mcp.example.test", 443, "/index.php"),
            parse_endpoint("https://mcp.example.test/index.php"),
        )
        for endpoint in (
            "http://mcp.example.test/index.php",
            "https://user:secret@mcp.example.test/index.php",
            "https://mcp.example.test/index.php?token=x",
            "https://mcp.example.test/index.php#fragment",
        ):
            with self.subTest(endpoint=endpoint), self.assertRaises(ValueError):
                parse_endpoint(endpoint)

    def test_public_preflight_requires_safe_https_endpoint(self):
        self.assertEqual(
            ("mcp.example.test", "/health.php", 443),
            parse_preflight_endpoint("https://mcp.example.test/health.php"),
        )
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_preflight_endpoint("http://mcp.example.test/health.php")

    def test_bearer_token_rejects_header_injection_characters(self):
        with self.assertRaisesRegex(ValueError, "characters unsupported"):
            HttpsPostTransport("https://mcp.example.test/index.php", "token\r\nX-Injected: yes")

    @patch("scripts.mcp_remote_acceptance.http.client.HTTPSConnection")
    def test_transport_sends_protocol_accept_auth_and_session_headers(self, connection_factory):
        response = connection_factory.return_value.getresponse.return_value
        response.status = 202
        response.read.return_value = b""
        response.getheaders.return_value = []
        transport = HttpsPostTransport("https://mcp.example.test/index.php", "valid-token")
        transport({"jsonrpc": "2.0", "method": "notifications/initialized"}, authenticated=True, session_id="sid")
        headers = connection_factory.return_value.request.call_args.kwargs["headers"]
        self.assertEqual("2025-11-25", headers.get("MCP-Protocol-Version"))
        self.assertEqual("application/json, text/event-stream", headers.get("Accept"))
        self.assertEqual("Bearer valid-token", headers.get("Authorization"))
        self.assertEqual("sid", headers.get("Mcp-Session-Id"))

    def test_decodes_json_and_server_sent_event_responses(self):
        payload = {"jsonrpc": "2.0", "id": 7, "result": {"tools": []}}
        self.assertEqual(payload["result"], decode_jsonrpc_response("application/json", json.dumps(payload).encode(), 7))
        event_body = f"event: message\ndata: {json.dumps(payload)}\n\n".encode()
        self.assertEqual(payload["result"], decode_jsonrpc_response("text/event-stream", event_body, 7))

    def test_rejects_response_with_unexpected_request_id(self):
        body = json.dumps({"jsonrpc": "2.0", "id": 8, "result": {}}).encode()
        with self.assertRaises(AcceptanceError):
            decode_jsonrpc_response("application/json", body, 7)

    def test_acceptance_checks_auth_initialize_tools_and_exact_skill_read(self):
        calls = []

        def post(payload, *, authenticated, session_id=None):
            calls.append((payload, authenticated, session_id))
            if not authenticated:
                return 401, {}, b""
            method = payload["method"]
            if method == "initialize":
                response = {
                    "jsonrpc": "2.0", "id": payload["id"],
                    "result": {
                        "protocolVersion": "2025-11-25",
                        "capabilities": {"tools": {}, "resources": {}},
                        "serverInfo": {"name": "ui-ux-pro-mcp", "version": "0.1.0"},
                    },
                }
                return 200, {"Mcp-Session-Id": "test-session", "Content-Type": "application/json"}, json.dumps(response).encode()
            if method == "notifications/initialized":
                return 202, {}, b""
            if method == "tools/list":
                response = {
                    "jsonrpc": "2.0", "id": payload["id"],
                    "result": {"tools": [{"name": name} for name in (
                        "list_uiux_skills", "search_uiux_guidance", "read_uiux_skill", "read_uiux_reference"
                    )]},
                }
                return 200, {"Content-Type": "application/json"}, json.dumps(response).encode()
            if method == "tools/call":
                response = {
                    "jsonrpc": "2.0", "id": payload["id"],
                    "result": {"content": [{"type": "text", "text": "---\nname: forms-input\n---"}]},
                }
                return 200, {"Content-Type": "application/json"}, json.dumps(response).encode()
            self.fail(f"unexpected method {method}")

        result = run_acceptance("https://mcp.example.test/index.php", post)
        self.assertEqual("ui-ux-pro-mcp", result["server_name"])
        self.assertEqual(4, result["tool_count"])
        self.assertEqual("forms-input", result["skill_read"])
        self.assertEqual(["initialize", "initialize", "notifications/initialized", "tools/list", "tools/call"],
                         [call[0]["method"] for call in calls])
        self.assertTrue(calls[0][1] is False)
        self.assertTrue(all(call[1] for call in calls[1:]))
        self.assertEqual("test-session", calls[-1][2])

    def test_acceptance_fails_if_endpoint_does_not_require_bearer_auth(self):
        def post(payload, *, authenticated, session_id=None):
            if not authenticated:
                body = json.dumps({"jsonrpc": "2.0", "id": 0, "result": {}}).encode()
                return 200, {"Content-Type": "application/json"}, body
            self.fail("authenticated request must not run after auth rejection fails")

        with self.assertRaisesRegex(AcceptanceError, "(?i)unauthenticated"):
            run_acceptance("https://mcp.example.test/index.php", post)

    def test_acceptance_refuses_redirects_after_authentication(self):
        calls = 0

        def post(payload, *, authenticated, session_id=None):
            nonlocal calls
            calls += 1
            if not authenticated:
                return 401, {}, b""
            return 302, {"Location": "https://other.example.test/collect"}, b""

        with self.assertRaisesRegex(AcceptanceError, "redirect refused"):
            run_acceptance("https://mcp.example.test/index.php", post)
        self.assertEqual(2, calls)


if __name__ == "__main__":
    unittest.main()
