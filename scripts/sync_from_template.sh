
#!/bin/bash

# Simple script to sync files from cursor-latex-zotero-template
# Run this from your project root directory

TEMPLATE_REPO="https://github.com/wusche1/cursor-latex-zotero-template.git"

echo "Syncing from template repository..."

# Clone template to temp directory
TEMP_DIR=$(mktemp -d)
git clone --depth 1 "$TEMPLATE_REPO" "$TEMP_DIR"

# Delete local scripts folder completely to ensure clean overwrite
echo "Removing local scripts folder..."
rm -rf scripts/

# Copy everything except excluded directories
rsync -av --exclude='content/' --exclude='bib/' --exclude='figures/' --exclude='lib/' --exclude='main.tex' --exclude='README.md' --exclude='.git/' "$TEMP_DIR/" ./

# Cleanup
rm -rf "$TEMP_DIR"

# Sync dependencies
echo "Syncing dependencies..."
uv sync

echo "Sync complete! Review changes with: git status" 
