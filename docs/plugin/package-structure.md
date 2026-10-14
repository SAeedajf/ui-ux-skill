# Package structure

The generated `plugins/ui-ux-pro/` directory is a portable Agent Plugins 1.0.0 package:

```text
plugins/ui-ux-pro/
├── plugin.json
├── LICENSE
└── skills/
    └── <skill-id>/
        ├── SKILL.md
        └── references/*.md
```

`config/ui-ux-pro.json` is the single package identity/version input. The standard manifest is generated from that input and checked against the vendored official JSON Schema in `schemas/agent-plugins/1.0.0/`. No Codex-only overlay, MCP server, hooks, credentials, or copied third-party publications are included. Skills and references are copied byte-for-byte from `.agents/skills/`; the repository CC BY 4.0 license text is included for distribution clarity.

The ZIP has the package root at its archive root. Entry order, timestamps, permissions and compression are fixed. The companion `.manifest.json` is outside the ZIP and records source commit, version, per-file SHA-256/size and archive SHA-256. This file describes provenance and structural validation only; it is not a signed attestation and does not certify installation or host execution.
