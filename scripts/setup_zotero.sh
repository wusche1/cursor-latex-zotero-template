#!/bin/bash

set -e

# Check if Zotero is already installed
if [ -d "/Applications/Zotero.app" ]; then
    echo "Zotero is already installed. Skipping to avoid changes to existing setup."
    exit 0
fi

# Install Homebrew if missing (prereq)
if ! command -v brew >/dev/null 2>&1; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# Install Zotero
brew install --cask zotero
echo "Zotero installed. Launching it to create initial profile..."
open -a Zotero
sleep 5  # Wait for initial launch

# After install, check for DB and create collection
DB_PATH="~/Zotero/zotero.sqlite"
COLLECTION_NAME="$(basename "$(pwd)")"

if [ ! -f "$DB_PATH" ]; then
    echo "Zotero database not found. Please open and close Zotero once to initialize it (skip signup if prompted). Then re-run this script."
    exit 1
fi

# Create collection if not exists
echo "Creating Zotero collection: $COLLECTION_NAME"
sqlite3 "$DB_PATH" <<EOF
INSERT OR IGNORE INTO collections (collectionName) VALUES ('$COLLECTION_NAME');
EOF
if [ $? -eq 0 ]; then
    echo "Collection created or already exists."
else
    echo "Failed to create collection."
fi

# Download latest Better BibTeX .xpi
XPI_URL=$(curl -s https://api.github.com/repos/retorquere/zotero-better-bibtex/releases/latest | grep "browser_download_url.*\.xpi" | cut -d '"' -f 4)
XPI_FILE="~/Downloads/better-bibtex.xpi"
curl -L "$XPI_URL" -o "$XPI_FILE"
echo "Downloaded Better BibTeX to $XPI_FILE"

# Print instructions for manual install/config
echo "
<<<<<<< HEAD
Now manually install and configure Better BibTeX (since CLI automation is risky):
1. Open Zotero.
2. Go to Tools > Add-ons.
3. Click the gear icon > Install Add-on From File.
4. Select $XPI_FILE and install. Restart Zotero.
5. Go to Tools > Better BibTeX > Preferences.
6. Set Citation key format to '[auth:lower][year]'.
7. Enable auto-export: Edit > Preferences > Better BibTeX > Automatic export.
8. Add your collection, set export as BibTeX to 'bib/refs.bib' in your project.
9. Enable 'Pin BibTeX key' for stable keys.
=======
Better BibTeX downloaded to $XPI_FILE

Now manually complete the Better BibTeX setup:
1. Open Zotero → Tools → Add-ons → Install Add-on From File (select the downloaded .xpi)
2. Restart Zotero
3. Go to Zotero → Settings →  Better BibTeX → Set Citation key format to `auth.lower +  year`
4. Add some sources to your collection (otherwise export won't work)
5. Right-click on your collection → Export Collection...
6. Choose format: Better BibTeX, enable 'Keep Updated', do NOT enable 'Export Files'
7. Click OK and save to 'bib/refs.bib' in your project (overwrite when prompted)
>>>>>>> 1ebc004 (remove pin bibtex key)
"
echo "Setup complete! Run the sync script next." 