#!/bin/bash

# Zotero Collection Sync Script
# Syncs PDFs, notes, and extracted text for a specific collection

# CONFIGURATION - EDIT THESE
COLLECTION_NAME="$(basename "$(dirname "$(dirname "$(realpath "$0")")")")"  # Name of your Zotero collection (auto-detected from project folder)
OUTPUT_DIR="$(dirname "$(dirname "$(realpath "$0")")")/bib"  # Where to save everything
ZOTERO_DATA_DIR="$HOME/Zotero"  # Your Zotero data directory
CHECK_INTERVAL=300  # Check every 5 minutes (in seconds)

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Log file
LOG_FILE="$OUTPUT_DIR/.sync_log.txt"

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to get collection ID from name
get_collection_id() {
    local collection_name="$1"
    sqlite3 "file:$ZOTERO_DATA_DIR/zotero.sqlite?immutable=1" <<EOF
SELECT collectionID FROM collections 
WHERE collectionName = '$collection_name' 
AND collectionID NOT IN (SELECT collectionID FROM deletedCollections);
EOF
}

# Function to sync collection
sync_collection() {
    log_message "Starting sync for collection: $COLLECTION_NAME"
    
    # Get collection ID
    COLLECTION_ID=$(get_collection_id "$COLLECTION_NAME")
    
    if [ -z "$COLLECTION_ID" ]; then
        log_message "ERROR: Collection '$COLLECTION_NAME' not found!"
        return 1
    fi
    
    # Get all items in collection
    sqlite3 "file:$ZOTERO_DATA_DIR/zotero.sqlite?immutable=1" <<EOF | while IFS='|' read -r itemID itemKey title firstAuthor year itemType; do
.mode list
.separator |
SELECT DISTINCT
    items.itemID,
    items.key,
    COALESCE(itemDataValues.value, 'Untitled') as title,
    COALESCE(creators.lastName, 'Unknown') as firstAuthor,
    COALESCE(SUBSTR(date.value, 1, 4), 'NoDate') as year,
    itemTypes.typeName
FROM items
JOIN collectionItems ON items.itemID = collectionItems.itemID
JOIN itemTypes ON items.itemTypeID = itemTypes.itemTypeID
LEFT JOIN itemData AS titleData ON items.itemID = titleData.itemID 
    AND titleData.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'title')
LEFT JOIN itemDataValues ON titleData.valueID = itemDataValues.valueID
LEFT JOIN itemCreators ON items.itemID = itemCreators.itemID AND itemCreators.orderIndex = 0
LEFT JOIN creators ON itemCreators.creatorID = creators.creatorID
LEFT JOIN itemData AS dateData ON items.itemID = dateData.itemID 
    AND dateData.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'date')
LEFT JOIN itemDataValues AS date ON dateData.valueID = date.valueID
WHERE collectionItems.collectionID = $COLLECTION_ID
AND items.itemID NOT IN (SELECT itemID FROM deletedItems)
AND itemTypes.typeName NOT IN ('attachment', 'note');
EOF
        # Get citation key from Better BibTeX database
        citationKey=$(sqlite3 "file:$ZOTERO_DATA_DIR/better-bibtex.sqlite?immutable=1" "SELECT citationKey FROM citationkey WHERE itemKey = '$itemKey';")
        if [ -z "$citationKey" ]; then
            citationKey="$itemKey"  # Fallback to Zotero key if no citation key found
        fi
        process_item "$itemID" "$itemKey" "$citationKey" "$title" "$firstAuthor" "$year" "$itemType"
    done
    
    log_message "Sync completed"
}

# Function to process each item
process_item() {
    local itemID="$1"
    local itemKey="$2"
    local citationKey="$3"
    local title="$4"
    local firstAuthor="$5"
    local year="$6"
    local itemType="$7"
    
    # Use citation key as folder name
    local folder_name="$citationKey"
    
    # Create item folder
    local item_dir="$OUTPUT_DIR/$folder_name"
    mkdir -p "$item_dir"
    
    # Get URL if available
    local url=$(sqlite3 "file:$ZOTERO_DATA_DIR/zotero.sqlite?immutable=1" "SELECT value FROM itemDataValues WHERE valueID = (SELECT valueID FROM itemData WHERE itemID = $itemID AND fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'url'));")
    
    # Save metadata
    echo "Title: $title" > "$item_dir/.metadata.txt"
    echo "Author: $firstAuthor" >> "$item_dir/.metadata.txt"
    echo "Year: $year" >> "$item_dir/.metadata.txt"
    echo "Type: $itemType" >> "$item_dir/.metadata.txt"
    echo "Citation Key: $citationKey" >> "$item_dir/.metadata.txt"
    echo "Zotero Key: $itemKey" >> "$item_dir/.metadata.txt"
    if [ -n "$url" ]; then
        echo "URL: $url" >> "$item_dir/.metadata.txt"
    fi
    
    # Process attachments (PDFs and snapshots)
    process_attachments "$itemID" "$item_dir" "$folder_name"
    
    # Process notes
    process_notes "$itemID" "$item_dir" "$folder_name"
}

# Function to process attachments (PDFs and snapshots)
process_attachments() {
    local itemID="$1"
    local item_dir="$2"
    local folder_name="$3"
    
    # Check if PDF already exists (to avoid reprocessing)
    local pdf_dest="$item_dir/${folder_name}.pdf"
    
    # First, try to find PDF attachments
    local pdf_processed=false
    sqlite3 "file:$ZOTERO_DATA_DIR/zotero.sqlite?immutable=1" <<EOF | while IFS='|' read -r attachmentKey path; do
.mode list
.separator |
SELECT 
    items.key,
    COALESCE(itemAttachments.path, '') as path
FROM items
JOIN itemAttachments ON items.itemID = itemAttachments.itemID
WHERE itemAttachments.parentItemID = $itemID
AND items.itemID NOT IN (SELECT itemID FROM deletedItems)
AND itemAttachments.contentType = 'application/pdf';
EOF
        if [ -n "$attachmentKey" ]; then
            # Check if it's a linked file or stored file
            if [[ "$path" == "storage:"* ]]; then
                # Stored file
                local pdf_file="$ZOTERO_DATA_DIR/storage/$attachmentKey/${path#storage:}"
            else
                # Linked file - might need base directory handling
                local pdf_file="$path"
            fi
            
            # If no path, check default location
            if [ -z "$path" ] || [ ! -f "$pdf_file" ]; then
                pdf_file="$ZOTERO_DATA_DIR/storage/$attachmentKey/*.pdf"
                pdf_file=$(ls $pdf_file 2>/dev/null | head -1)
            fi
            
            if [ -f "$pdf_file" ]; then
                # Copy PDF
                if [ ! -f "$pdf_dest" ] || [ "$pdf_file" -nt "$pdf_dest" ]; then
                    cp "$pdf_file" "$pdf_dest"
                    log_message "  Copied PDF: $folder_name.pdf"
                fi
                
                # Extract text
                local text_dest="$item_dir/${folder_name}_fulltext.md"
                if [ ! -f "$text_dest" ] || [ "$pdf_file" -nt "$text_dest" ]; then
                    echo "# Full Text: $folder_name" > "$text_dest"
                    echo "" >> "$text_dest"
                    echo "Extracted: $(date '+%Y-%m-%d %H:%M:%S')" >> "$text_dest"
                    echo "Source: PDF" >> "$text_dest"
                    echo "---" >> "$text_dest"
                    echo "" >> "$text_dest"
                    pdftotext -layout "$pdf_file" - >> "$text_dest" 2>/dev/null
                    log_message "  Extracted text: ${folder_name}_fulltext.md"
                fi
                
                break
            fi
        fi
    done
    
    # If no PDF was found, look for HTML snapshots
    if [ ! -f "$pdf_dest" ]; then
        sqlite3 "file:$ZOTERO_DATA_DIR/zotero.sqlite?immutable=1" <<EOF | while IFS='|' read -r attachmentKey path title; do
.mode list
.separator |
SELECT 
    items.key,
    COALESCE(itemAttachments.path, '') as path,
    COALESCE(titleValues.value, 'Snapshot') as title
FROM items
JOIN itemAttachments ON items.itemID = itemAttachments.itemID
LEFT JOIN itemData AS titleData ON items.itemID = titleData.itemID 
    AND titleData.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'title')
LEFT JOIN itemDataValues AS titleValues ON titleData.valueID = titleValues.valueID
WHERE itemAttachments.parentItemID = $itemID
AND items.itemID NOT IN (SELECT itemID FROM deletedItems)
AND itemAttachments.contentType = 'text/html';
EOF
            if [ -n "$attachmentKey" ]; then
                local snapshot_dir="$ZOTERO_DATA_DIR/storage/$attachmentKey"
                local html_file=""
                
                # Look for HTML files in the snapshot directory
                if [ -d "$snapshot_dir" ]; then
                    html_file=$(find "$snapshot_dir" -name "*.html" -o -name "*.htm" | head -1)
                fi
                
                if [ -f "$html_file" ]; then
                    # Copy the original HTML file
                    local html_dest="$item_dir/${folder_name}.html"
                    if [ ! -f "$html_dest" ] || [ "$html_file" -nt "$html_dest" ]; then
                        cp "$html_file" "$html_dest"
                        log_message "  Copied HTML: ${folder_name}.html"
                    fi
                    
                    # Extract and convert HTML to markdown
                    local text_dest="$item_dir/${folder_name}_fulltext.md"
                    if [ ! -f "$text_dest" ] || [ "$html_file" -nt "$text_dest" ]; then
                        echo "# Full Text: $folder_name" > "$text_dest"
                        echo "" >> "$text_dest"
                        echo "Extracted: $(date '+%Y-%m-%d %H:%M:%S')" >> "$text_dest"
                        echo "Source: HTML Snapshot" >> "$text_dest"
                        echo "---" >> "$text_dest"
                        echo "" >> "$text_dest"
                        
                        # Convert HTML to markdown using pandoc if available
                        if command -v pandoc >/dev/null 2>&1 && command -v jq >/dev/null 2>&1 && command -v perl >/dev/null 2>&1; then
                            # Extract JSON-LD structured data and convert to markdown using Perl
                            if perl -0777 -ne 'print $1 if /<script type=application\/ld\+json>(.*?)<\/script>/s' "$html_file" | jq -r '.text' >/dev/null 2>&1; then
                                # Extract JSON-LD text content using Perl multiline regex (exact method from user)
                                perl -0777 -ne 'print $1 if /<script type=application\/ld\+json>(.*?)<\/script>/s' "$html_file" | \
                                    jq -r '.text' | \
                                    pandoc -f html -t markdown >> "$text_dest" 2>/dev/null
                            else
                                # Regular HTML to markdown conversion
                                pandoc -f html -t markdown "$html_file" >> "$text_dest" 2>/dev/null
                            fi
                        elif command -v lynx >/dev/null 2>&1; then
                            lynx -dump -nolist "$html_file" >> "$text_dest" 2>/dev/null
                        elif command -v w3m >/dev/null 2>&1; then
                            w3m -dump "$html_file" >> "$text_dest" 2>/dev/null
                        else
                            # Fallback: basic HTML stripping
                            sed 's/<[^>]*>//g' "$html_file" | sed 's/&nbsp;/ /g' | sed 's/&lt;/</g' | sed 's/&gt;/>/g' | sed 's/&amp;/\&/g' >> "$text_dest"
                        fi
                        
                        log_message "  Extracted and converted HTML to markdown: ${folder_name}_fulltext.md"
                    fi
                    break
                fi
            fi
        done
    fi
}

# Function to process notes
process_notes() {
    local itemID="$1"
    local item_dir="$2"
    local folder_name="$3"
    
    # Get all notes for this item
    local notes_file="$item_dir/${folder_name}_notes.md"
    local has_notes=false
    
    # Start notes file
    echo "# Notes: $folder_name" > "$notes_file.tmp"
    echo "" >> "$notes_file.tmp"
    echo "Last Updated: $(date '+%Y-%m-%d %H:%M:%S')" >> "$notes_file.tmp"
    echo "---" >> "$notes_file.tmp"
    echo "" >> "$notes_file.tmp"
    
    # Get notes
    sqlite3 "file:$ZOTERO_DATA_DIR/zotero.sqlite?immutable=1" <<EOF | while IFS='|' read -r note dateAdded; do
.mode list
.separator |
SELECT 
    itemNotes.note,
    items.dateAdded
FROM items
JOIN itemNotes ON items.itemID = itemNotes.itemID
WHERE itemNotes.parentItemID = $itemID
AND items.itemID NOT IN (SELECT itemID FROM deletedItems)
ORDER BY items.dateAdded;
EOF
        if [ -n "$note" ]; then
            has_notes=true
            echo "## Note from $dateAdded" >> "$notes_file.tmp"
            echo "" >> "$notes_file.tmp"
            # Convert HTML to markdown (basic)
            echo "$note" | \
                sed 's/<br>/\n/g' | \
                sed 's/<\/p>/\n\n/g' | \
                sed 's/<p>//g' | \
                sed 's/<[^>]*>//g' | \
                sed 's/&nbsp;/ /g' | \
                sed 's/&lt;/</g' | \
                sed 's/&gt;/>/g' | \
                sed 's/&amp;/\&/g' >> "$notes_file.tmp"
            echo "" >> "$notes_file.tmp"
            echo "---" >> "$notes_file.tmp"
            echo "" >> "$notes_file.tmp"
        fi
    done
    
    # Only create notes file if there are notes
    if [ -s "$notes_file.tmp" ] && grep -q "## Note from" "$notes_file.tmp"; then
        mv "$notes_file.tmp" "$notes_file"
        log_message "  Exported notes: ${folder_name}_notes.md"
    else
        rm -f "$notes_file.tmp"
        rm -f "$notes_file"  # Remove old notes file if no notes exist
    fi
}

# Main daemon loop
run_daemon() {
    log_message "=== Zotero Collection Sync Started ==="
    log_message "Collection: $COLLECTION_NAME"
    log_message "Output: $OUTPUT_DIR"
    log_message "Check interval: $CHECK_INTERVAL seconds"
    
    # Check if Zotero database exists
    if [ ! -f "$ZOTERO_DATA_DIR/zotero.sqlite" ]; then
        log_message "ERROR: Zotero database not found at $ZOTERO_DATA_DIR/zotero.sqlite"
        exit 1
    fi
    
    # Initial sync
    sync_collection
    
    # Keep running
    while true; do
        sleep $CHECK_INTERVAL
        sync_collection
    done
}

# Handle script termination
trap 'log_message "Script terminated"; exit 0' SIGINT SIGTERM

# Start the daemon
run_daemon