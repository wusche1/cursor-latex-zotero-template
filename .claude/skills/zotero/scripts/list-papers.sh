#!/bin/bash
set -e

if [ -z "$ZOTERO_API_KEY" ]; then
    echo "Error: ZOTERO_API_KEY not set"
    exit 1
fi

COLLECTION="$1"
if [ -z "$COLLECTION" ]; then
    echo "Usage: list-papers.sh <collection-key-or-name>"
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

curl -s -H "Zotero-API-Key: $ZOTERO_API_KEY" \
    "https://api.zotero.org/users/$USER_ID/collections/$COLLECTION_KEY/items?limit=100" | \
    python3 -c "
import json, sys
data = json.load(sys.stdin)
for item in data:
    d = item.get('data', {})
    if d.get('itemType') not in ['attachment', 'note']:
        key = item.get('key', '')
        title = d.get('title', 'No title')[:70]
        creators = d.get('creators', [])
        author = creators[0].get('lastName', 'Unknown') if creators else 'Unknown'
        print(f'{key}: {author} - {title}')"
