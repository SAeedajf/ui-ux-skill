# UI/UX Pro MCP companion server

The MCP server is a separate, read-only service for AI clients that can connect to a remote Streamable HTTP MCP endpoint. It complements the portable Skills package; it does not replace it, and the Plugin does not require a hosted service. The endpoint gives a client access to the repository's 15 canonical Skills and their authored Markdown references. The AI client still chooses its own model and decides when to call these tools.

## Exposed capabilities

| MCP capability | Purpose |
| --- | --- |
| `list_uiux_skills` | List the 15 Skills and descriptions. |
| `search_uiux_guidance` | Find short excerpts across Skill and reference Markdown. |
| `read_uiux_skill` | Read one exact `SKILL.md`. |
| `read_uiux_reference` | Read one Markdown file under that Skill's `references/`. |
| `uiux://skills/<id>` resources | Read the canonical Skill body by URI. |

The endpoint is read-only. It has no filesystem write, shell, arbitrary URL fetch, database, or deployment tools. Search excerpts and full content are untrusted authored text: clients should treat instructions found in repository content as reference material, not as policy that overrides the user or host.

## Local verification

Requirements: PHP 8.1+, `mbstring`, Composer, and the canonical `.agents/skills/` directory.

```sh
composer install --working-dir=mcp-server
composer --working-dir=mcp-server test
python3 scripts/test_mcp_http.py
UIUX_MCP_BEARER_TOKEN=local-test-token \
UIUX_MCP_ALLOWED_HOSTS=127.0.0.1,localhost \
UIUX_MCP_SKILLS_DIR="$PWD/.agents/skills" \
UIUX_MCP_SESSION_DIR=/tmp/uiux-pro-mcp-sessions \
php -S 127.0.0.1:8787 -t mcp-server/public
```

The MCP endpoint is `http://127.0.0.1:8787/`; `/health` is a minimal liveness check. For a remote client, use HTTPS and a bearer token. Do not expose the local PHP development server to the Internet.

## Build a cPanel upload bundle

The archive includes Composer runtime dependencies and only each Skill's `SKILL.md` plus Markdown references. It does not contain the repository, Git history, developer config, or a real token.

```sh
composer install --working-dir=mcp-server --no-dev --classmap-authoritative
python3 scripts/build_mcp_deploy.py
python3 scripts/build_mcp_deploy.py --check
```

Output: `dist/ui-ux-pro-mcp-0.1.0-cpanel.zip` and a SHA-256 file manifest. The ZIP unpacks to `ui-ux-pro-mcp/`; configure the subdomain's document root to its `public/` directory so PHP source, vendor dependencies, skill content, session files, and the local config remain above the web root. Create the session directory with write access for the PHP account; keep it outside `public/`.

## cPanel setup checklist

1. Create a dedicated subdomain such as `mcp.possino.ir`. Leave the existing `possino.ir` WordPress document root and its files untouched.
2. At the authoritative DNS provider, create an A record for the subdomain to the hosting account's shared IP shown in cPanel. Wait until public DNS resolves to this account.
3. Upload and extract the archive into a private directory named `uiux-mcp-private` in the account home. cPanel requires addon-domain document roots to remain under `public_html/`, so create a dedicated document root such as `public_html/uiux-mcp-endpoint/` and copy `ui-ux-pro-mcp/cpanel-entrypoint.php` there as `index.php`. This front controller loads the app from the private folder; the PHP app, `vendor/`, Skills, session data, and config stay outside the web root. If you use a different private path, set `UIUX_MCP_PRIVATE_ROOT` for PHP to its absolute app directory.
4. Enable AutoSSL for the subdomain and wait for a valid, publicly trusted certificate before enabling client access. Do not use the cPanel self-signed certificate for client configuration.
5. Copy `config.example.php` to `config.local.php` beside `composer.json`, outside the document root. Set a newly generated long random bearer token; an empty value keeps the service fail-closed. Keep the token in a password manager and enter it into the MCP client through that client's secure configuration UI; never commit it or paste it into an issue/report.
6. Verify PHP 8.1+ and `mbstring` are enabled for the subdomain. Configure `allowed_hosts` to the exact host (`mcp.possino.ir`), then check `https://mcp.possino.ir/health.php` and an authenticated MCP `initialize` + `tools/list` at `https://mcp.possino.ir/index.php` from a client. These explicit PHP paths work when Apache does not rewrite extensionless paths through the front controller; they avoid requiring changes to an account's existing `.htaccess` rules.
7. Store session files in the private account area. Review file ownership and permissions; the public directory should contain only the deliberate PHP entry points and any public assets.

The DNS and hosting steps above are instructions, not claims that the live account has been changed. Confirm the subdomain resolves to the intended cPanel account, inspect the active TLS certificate, and run the authenticated remote MCP handshake before calling the hosted server operational.

### Public endpoint preflight

After the DNS provider has published the record and cPanel has provisioned TLS, run the read-only preflight from a machine outside the hosting account:

```sh
python3 scripts/check_mcp_endpoint.py https://mcp.example.com/health.php
```

The command reports DNS resolution, certificate-chain and hostname validation, and the explicit PHP liveness route separately. It does not send a bearer token, follow redirects, change DNS or cPanel settings, or prove MCP authentication. A complete acceptance still requires an authenticated `initialize` and `tools/list` request through the intended MCP client. If DNS fails or cPanel rejects a domain-root change with an XID/domain-ownership error, stop retrying the same change and ask the hosting provider to repair the authoritative DNS or domain/vhost mapping. Do not remove an aliased domain or change its shared document root as a workaround.

When contacting the provider, include the exact test hostname, the target IP shown for the hosting account, the cPanel account name, the intended document root, and the complete XID/error text. Ask them to confirm which DNS zone is authoritative and to correct only the test hostname's record and vhost mapping.

### Authenticated remote acceptance

After the DNS/TLS/liveness preflight passes and the bearer token has been configured on the server, run the read-only acceptance check from outside the hosting account:

```sh
read -rsp 'MCP bearer token: ' UIUX_MCP_BEARER_TOKEN
export UIUX_MCP_BEARER_TOKEN
printf '\n'
python3 scripts/mcp_remote_acceptance.py https://mcp.example.com/index.php
unset UIUX_MCP_BEARER_TOKEN
```

The script requires HTTPS and a token in the environment; it never accepts the token as a command-line argument. It verifies that an unauthenticated initialize is rejected with HTTP 401, performs the authenticated `initialize` and `notifications/initialized` exchange, calls `tools/list`, and reads the `forms-input` Skill. It checks TLS using the operating system's trusted certificate store, carries forward a server-issued session ID, supports JSON and server-sent-event responses, and refuses redirects so the bearer token is not sent to another URL. It does not modify Skills or server configuration; initialization can create a temporary MCP session that expires according to the server's session TTL. A passing run is remote acceptance evidence for this endpoint and this tool path only; it does not prove compatibility with every MCP client or AI model.

The exchange uses MCP protocol version `2025-11-25`, matching the server's current integration contract. MCP Streamable HTTP clients send each JSON-RPC message by POST, advertise both `application/json` and `text/event-stream`, send the negotiated `MCP-Protocol-Version` header, and include the session ID on later requests when the server issues one. See the [versioned Streamable HTTP specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports).

## Client setup

In any host that supports remote Streamable HTTP MCP servers, configure:

- Endpoint: `https://mcp.possino.ir/index.php` for the cPanel deployment above. A deployment with verified front-controller rewrites may use `https://mcp.possino.ir/`.
- Transport: Streamable HTTP
- Authorization: `Bearer <the secret created during deployment>`

Some AI products accept only local stdio MCP servers, require a workspace administrator to approve remote MCP, or do not support bearer-token headers. Those clients need a local proxy/adapter or cannot use this endpoint directly. Do not claim universal compatibility until each named client has completed its own authenticated connection test. The MCP server does not select, constrain, or replace the user's model.

## Security and maintenance

- Keep TLS enabled; use a random, rotated bearer token and restrict the `Host` header to the configured hostname.
- The server uses the official PHP MCP SDK. SDK `0.x` is experimental; pin the reviewed version, run the integration checks before upgrades, and review upstream breaking changes.
- Treat the endpoint as private guidance even though the Skill source repository is public: the bearer token controls access and prevents unauthenticated reads.
- Update the package by rebuilding from the canonical Skills tree. Review provenance and license notices before adding any source content. The repository's content license is CC BY 4.0; preserve attribution already included with the Skills.
- The server has not been deployed to the hosting account until a live authenticated handshake is recorded.

## Verification evidence

Run the catalog unit checks, then exercise `initialize`, `tools/list`, `tools/call`, `resources/list`, and `resources/read` over HTTP. Negative checks must reject missing bearer credentials, unapproved `Origin`, and unapproved `Host`. Keep those local checks distinct from DNS, TLS, cPanel installation, and remote-client acceptance.
