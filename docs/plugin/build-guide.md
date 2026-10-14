# Build UI/UX Pro

The canonical Skills live under `.agents/skills/`; `plugins/ui-ux-pro/` is generated. Edit the canonical source, then rebuild and validate. No network access or model/API credentials are used by the builder.

## Setup and commands

Python 3.12+ is used in CI. Install the pinned developer-only validation dependencies:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/build-plugin.py
python3 scripts/validate-plugin.py
python3 scripts/build-plugin.py --check
python3 -m unittest discover -s tests -v
python3 scripts/build-plugin.py --check --archive
```

`--check` is read-only and fails if generated files differ from the canonical source. `--archive` writes a reproducible ZIP and a provenance JSON under ignored `dist/`; the provenance records the current full Git commit SHA. Commit source and generated plugin files before archiving so the SHA identifies the source commit. CI performs these same checks and retains the ZIP plus sidecar as a workflow artifact. It does not publish a release or install the plugin into a host.

For structural validation of an already-extracted package independent of this repository's source tree:

```sh
python3 scripts/validate-plugin.py --package /path/to/extracted/package --structure-only
```

This checks package schema, skill format, references, unsafe paths, symlinks and secret-like material. It does not prove host discovery, installation, activation, or runtime behavior.
