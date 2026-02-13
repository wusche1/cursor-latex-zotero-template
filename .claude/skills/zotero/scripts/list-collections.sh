#!/bin/bash
set -e

if [ -z "$ZOTERO_API_KEY" ]; then
    echo "Error: ZOTERO_API_KEY not set"
    exit 1
fi

USER_ID=$(curl -s -H "Zotero-API-Key: $ZOTERO_API_KEY" \
    "https://api.zotero.org/keys/$ZOTERO_API_KEY" | \
    python3 -c "import json,sys; print(json.load(sys.stdin)['userID'])")

curl -s -H "Zotero-API-Key: $ZOTERO_API_KEY" \
    "https://api.zotero.org/users/$USER_ID/collections" | \
    python3 -c "
import json, sys
data = json.load(sys.stdin)
for c in sorted(data, key=lambda x: x['data']['name'].lower()):
    print(f\"{c['data']['key']}: {c['data']['name']}\")"
