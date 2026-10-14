# Migrating duplicate legacy Skills

When both the plugin and legacy Skills are discoverable, Codex exposes both namespaces: plugin entries use names such as `ui-ux-pro:interface-layout`; legacy entries use unprefixed names such as `interface-layout`. In the isolated three-scenario probe, Plugin Only produced 15 plugin-prefixed skills, Legacy Only produced 15 unprefixed skills, and Both produced both sets. This proves duplicate discovery, but without an authenticated model trace it does not establish precedence, actual selection, or measurable context cost.

## Recommended migration

Prefer the plugin as the maintained source after confirming its installation and discovery. Preserve the legacy copies in a reversible archive outside any directory scanned for skills. Do not delete the user's skill files automatically.

1. List and inspect the existing legacy skill directories. Confirm the 15 IDs and identify any local edits before moving anything.
2. Make a timestamped backup outside scanned skill roots, for example `~/.agents/skills-backup/ui-ux-skill-YYYYMMDD/`.
3. Move only the matching legacy UI/UX skill directories into that backup. Do not remove unrelated skills or edit `~/.codex/config.toml`.
4. Start a fresh Codex session and inspect skill discovery. Expect one plugin-prefixed entry per UI/UX skill.
5. If discovery or behavior regresses, move the saved directories back to their original locations and restart Codex. Keep the plugin installed or remove it separately according to the installation guide.

Example commands are intentionally presented as a sequence to review and adapt, not as an automatic cleanup script:

```sh
mkdir -p "$HOME/.agents/skills-backup/ui-ux-skill-$(date +%Y%m%d)"
# Move only the confirmed legacy UI/UX skill directories into that backup.
# To roll back, move those same directories back to their original locations.
```

Do not run broad commands such as `rm -rf ~/.agents/skills/*`. The exact legacy skill locations vary by user and may contain edits or unrelated skills. Test migration first in a disposable HOME.

## Discovery test matrix

| Scenario | Result | Interpretation |
|---|---|---|
| Plugin Only | 15 `ui-ux-pro:` entries | Plugin skill discovery works in CLI diagnostic input. |
| Legacy Only | 15 unprefixed entries | Existing skill discovery remains available. |
| Both | Both 15-entry sets appear | Duplicate discovery is observable; precedence/selection is unknown. |
