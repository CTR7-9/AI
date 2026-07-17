# Ingest script (excerpt)

#!/bin/bash
# Normalize new files and update index
./scripts/normalize.sh
python3 scripts/index_new.py --path skills-archive

(Excerpt of ingest automation)