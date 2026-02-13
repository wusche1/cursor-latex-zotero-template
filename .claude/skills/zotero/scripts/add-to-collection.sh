#!/bin/bash
set -e

if [ -z "$ZOTERO_API_KEY" ]; then
    echo "Error: ZOTERO_API_KEY not set"
    exit 1
fi

COLLECTION="$1"
shift
ITEM_KEYS=("$@")

if [ -z "$COLLECTION" ] || [ ${#ITEM_KEYS[@]} -eq 0 ]; then
    echo "Usage: add-to-collection.sh <collection-key-or-name> <item-key> [item-key...]"
    exit 1
fi

USER_ID=$(curl -s -H "Zotero-API-Key: $ZOTERO_API_KEY" \
    "https://api.zotero.org/keys/$ZOTERO_API_KEY" | \
    python3 -c "import json,sys; print(json.load(sys.stdin)['userID'])")

# Resolve collection name to key if needed
COLLECTION_KEY=$(curl -s -H "Zotero-API-Key: $ZOTERO_API_KEY" \
    "https://api.zotero.org/users/$USER_ID/collections" | \
    python3 -c "
import json, sys
data = json.load(sys.stdin)
query = '$COLLECTION'
for c in data:
    if c['data']['key'] == query or c['data']['name'].lower() == query.lower():
        print(c['data']['key'])
        break
")

if [ -z "$COLLECTION_KEY" ]; then
    echo "Error: Collection '$COLLECTION' not found"
    exit 1
fi

for KEY in "${ITEM_KEYS[@]}"; do
    ITEM=$(curl -s -H "Zotero-API-Key: $ZOTERO_API_KEY" \
        "https://api.zotero.org/users/$USER_ID/items/$KEY")

    VERSION=$(echo "$ITEM" | python3 -c "import json,sys; print(json.load(sys.stdin)['version'])")
    COLLECTIONS=$(echo "$ITEM" | python3 -c "
import json,sys
d = json.load(sys.stdin)['data']
c = d.get('collections', [])
c.append('$COLLECTION_KEY')
print(json.dumps(list(set(c))))")

    curl -s -X PATCH \
        -H "Zotero-API-Key: $ZOTERO_API_KEY" \
        -H "Content-Type: application/json" \
        -H "If-Unmodified-Since-Version: $VERSION" \
        -d "{\"collections\": $COLLECTIONS}" \
        "https://api.zotero.org/users/$USER_ID/items/$KEY" > /dev/null

    echo "Added $KEY to collection"
done
