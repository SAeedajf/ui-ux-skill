#!/usr/bin/env python3
"""Check public DNS, HTTPS certificate validation, and the MCP liveness route."""

from __future__ import annotations

import argparse
import http.client
import json
import socket
import ssl
import sys
from urllib.parse import urlsplit


def parse_endpoint(value: str) -> tuple[str, str, int]:
    parsed = urlsplit(value)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise argparse.ArgumentTypeError("Endpoint must be an HTTPS URL without credentials.")
    if parsed.query or parsed.fragment:
        raise argparse.ArgumentTypeError("Endpoint must not include a query string or fragment.")
    try:
        port = parsed.port or 443
    except ValueError as error:
        raise argparse.ArgumentTypeError("Endpoint must use a valid port.") from error
    path = parsed.path or "/health.php"
    if not path.startswith("/") or any(ord(character) < 32 for character in path):
        raise argparse.ArgumentTypeError("Endpoint path must be absolute and contain no control characters.")
    return parsed.hostname, path, port


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only preflight for public MCP endpoint DNS, TLS, and liveness."
    )
    parser.add_argument("endpoint", type=parse_endpoint, help="HTTPS endpoint, e.g. https://mcp.example.com/health.php")
    parser.add_argument("--timeout", type=float, default=8.0, help="Per-connection timeout in seconds (default: 8)")
    args = parser.parse_args()
    host, path, port = args.endpoint
    if not 1 <= args.timeout <= 30:
        parser.error("--timeout must be between 1 and 30 seconds")

    try:
        addresses = sorted({item[4][0] for item in socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)})
    except socket.gaierror as error:
        print(f"DNS: BLOCKED ({error})")
        print("TLS: NOT RUN")
        print("HTTPS health: NOT RUN")
        return 1
    print(f"DNS: PASS ({', '.join(addresses)})")

    context = ssl.create_default_context()
    connection = http.client.HTTPSConnection(host, port, timeout=args.timeout, context=context)
    try:
        connection.connect()
        tls_version = connection.sock.version() if connection.sock else "unknown"
        print(f"TLS: PASS ({tls_version}; certificate chain and hostname verified)")
        connection.request("GET", path, headers={"Accept": "application/json", "Cache-Control": "no-cache"})
        response = connection.getresponse()
        body = response.read(4096)
        content_type = response.getheader("Content-Type", "")
        if response.status != 200:
            print(f"HTTPS health: BLOCKED (HTTP {response.status}; redirect responses are not followed)")
            return 1
        try:
            payload = json.loads(body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            print(f"HTTPS health: BLOCKED (HTTP 200 but response is not JSON; Content-Type: {content_type or 'missing'})")
            return 1
        if not isinstance(payload, dict) or payload.get("status") != "ok" or payload.get("service") != "ui-ux-pro-mcp":
            print("HTTPS health: BLOCKED (response did not identify a healthy ui-ux-pro-mcp service)")
            return 1
        print("HTTPS health: PASS (public liveness route responded)")
        print("MCP authentication and initialize/tools/list: NOT CHECKED")
        return 0
    except (OSError, ssl.SSLError, http.client.HTTPException) as error:
        print(f"TLS/HTTPS health: BLOCKED ({type(error).__name__}: {error})")
        return 1
    finally:
        connection.close()


if __name__ == "__main__":
    sys.exit(main())
