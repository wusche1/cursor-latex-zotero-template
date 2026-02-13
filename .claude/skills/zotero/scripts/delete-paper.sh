#!/bin/bash
set -e

if [ -z "$ZOTERO_API_KEY" ]; then
    echo "Error: ZOTERO_API_KEY not set"
    exit 1
fi

if [ $# -lt 1 ]; then
    echo "Usage: delete-paper.sh <item-key> [item-key...]"
    exit 1
fi

USER_ID=$(curl -s -H "Zotero-API-Key: $ZOTERO_API_KEY" \
    "https://api.zotero.org/keys/$ZOTERO_API_KEY" | \
    python3 -c "import json,sys; print(json.load(sys.stdin)['userID'])")

for KEY in "$@"; do
    VERSION=$(curl -s -H "Zotero-API-Key: $ZOTERO_API_KEY" \
        "https://api.zotero.org/users/$USER_ID/items/$KEY" | \
        python3 -c "import json,sys; print(json.load(sys.stdin)['version'])")

    curl -s -X DELETE \
        -H "Zotero-API-Key: $ZOTERO_API_KEY" \
        -H "If-Unmodified-Since-Version: $VERSION" \
        "https://api.zotero.org/users/$USER_ID/items/$KEY"

    echo "Deleted $KEY"
done
