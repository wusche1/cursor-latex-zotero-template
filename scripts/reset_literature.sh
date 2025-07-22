#!/bin/bash

# Script to reset the literature database by removing all papers and embeddings
# Run this from your project root directory

echo "WARNING: This will delete all local literature data and embeddings!"
echo "Your Zotero library will NOT be affected - only local extracted files will be removed."
echo "You will need to re-run the extraction and embedding scripts, which may take time."
echo ""
read -p "Are you sure you want to continue? (y/N): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Operation cancelled."
    exit 0
fi

echo "Resetting literature database..."

# Delete all folders in bib/ directory (keeping refs.bib file)
echo "Removing all paper folders from bib/..."
find bib/ -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +

# Delete embeddings folder if it exists
if [ -d "embeddings" ]; then
    echo "Removing embeddings folder..."
    rm -rf embeddings/
fi

# Clear refs.bib file but keep it existing (just make it empty)
echo "Clearing refs.bib file..."
> bib/refs.bib

echo ""
echo "Literature reset complete!"
echo "- All paper folders removed from bib/"
echo "- Embeddings folder removed"
echo "- refs.bib file cleared"
echo ""
echo "You can now re-sync your literature with the Zotero sync scripts." 