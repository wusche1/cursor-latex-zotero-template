#!/bin/bash

set -e

# Check if Zotero is already installed
if [ -d "/Applications/Zotero.app" ]; then
    echo "Zotero is already installed. Continuing with setup..."
else
    # Install Zotero
    brew install --cask zotero
    echo "Zotero installed. Launching it to create initial profile..."
    open -a Zotero
    sleep 5  # Wait for initial launch
fi

# After install, check for DB and create collection
DB_PATH="~/Zotero/zotero.sqlite"
# Expand tilde to full path
DB_PATH="${DB_PATH/#\~/$HOME}"
COLLECTION_NAME="$(basename "$(pwd)")"

if [ ! -f "$DB_PATH" ]; then
    echo "Zotero database not found. Please open and close Zotero once to initialize it (skip signup if prompted). Then re-run this script."
    exit 1
fi

# Check if collection already exists
COLLECTION_EXISTS=$(sqlite3 "$DB_PATH" "SELECT COUNT(*) FROM collections WHERE collectionName = '$COLLECTION_NAME';")

if [ "$COLLECTION_EXISTS" -eq 0 ]; then
    echo "Creating Zotero collection: $COLLECTION_NAME"
    # Generate a random 8-character key for the collection
    COLLECTION_KEY=$(openssl rand -hex 4 | tr '[:lower:]' '[:upper:]')
    sqlite3 "$DB_PATH" "INSERT INTO collections (collectionName, libraryID, key) VALUES ('$COLLECTION_NAME', 1, '$COLLECTION_KEY');"
    if [ $? -eq 0 ]; then
        echo "Collection '$COLLECTION_NAME' created successfully."
    else
        echo "Failed to create collection."
        exit 1
    fi
else
    echo "Collection '$COLLECTION_NAME' already exists. Skipping creation."
fi

# Download latest Better BibTeX .xpi
XPI_URL=$(curl -s https://api.github.com/repos/retorquere/zotero-better-bibtex/releases/latest | grep "browser_download_url.*\.xpi" | cut -d '"' -f 4)
XPI_FILE="~/Downloads/better-bibtex.xpi"
# Expand tilde to full path
XPI_FILE="${XPI_FILE/#\~/$HOME}"
curl -L "$XPI_URL" -o "$XPI_FILE"
echo "Downloaded Better BibTeX to $XPI_FILE"

# Print instructions for manual install/config
echo "
Better BibTeX downloaded to $XPI_FILE

Now manually complete the Better BibTeX setup:
1. Open Zotero → Tools → Add-ons → Install Add-on From File (select the downloaded .xpi)
2. Restart Zotero
3. Go to Tools → Better BibTeX → Preferences → Set Citation key format to [auth:lower][year]
4. Enable 'Pin BibTeX key' for stable keys
5. Add some sources to your collection (otherwise export won't work)
6. Right-click on your collection → Export Collection...
7. Choose format: Better BibTeX, enable 'Keep Updated', do NOT enable 'Export Files'
8. Click OK and save to 'bib/refs.bib' in your project (overwrite when prompted)
"
echo "Setup complete! Run the sync script next with: uv run python scripts/main.py" 