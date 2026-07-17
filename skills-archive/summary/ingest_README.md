# Archive ingestion README (excerpt)

To ingest new harvested files into the archive, run the ingest script located at scripts/ingest.sh which processes manifests, normalizes paths, and updates the main index.

Usage:
```
./scripts/ingest.sh --source=./harvested --manifest=skills-archive/manifest-2026-07-16.md
```

(Internal archive tooling instructions)