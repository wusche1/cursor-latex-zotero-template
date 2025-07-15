#!/bin/bash

# Selective merge script that excludes specific directories
# Usage: ./selective_merge.sh <source-branch> [<target-branch>]

SOURCE_BRANCH="${1:-example-paper}"
TARGET_BRANCH="${2:-main}"
EXCLUDE_DIRS=("content" "figures" "bib")

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Selective merge from $SOURCE_BRANCH to $TARGET_BRANCH${NC}"
echo -e "${YELLOW}Excluding: ${EXCLUDE_DIRS[@]}${NC}"
echo ""

# Function to check if a file should be excluded
should_exclude() {
    local file="$1"
    for dir in "${EXCLUDE_DIRS[@]}"; do
        if [[ "$file" == "$dir/"* ]]; then
            return 0
        fi
    done
    return 1
}

# Ensure we're on the target branch
echo -e "${GREEN}Switching to $TARGET_BRANCH branch...${NC}"
git checkout "$TARGET_BRANCH" || exit 1

# Get list of modified and added files
echo -e "${GREEN}Finding modified and added files...${NC}"
MODIFIED_FILES=$(git diff --name-only --diff-filter=AM "$TARGET_BRANCH..$SOURCE_BRANCH")

# Get list of deleted files
echo -e "${GREEN}Finding deleted files...${NC}"
DELETED_FILES=$(git diff --name-only --diff-filter=D "$TARGET_BRANCH..$SOURCE_BRANCH")

# Process modified/added files
echo -e "${GREEN}Processing modified/added files...${NC}"
while IFS= read -r file; do
    if [[ -n "$file" ]] && ! should_exclude "$file"; then
        echo "  Checking out: $file"
        git checkout "$SOURCE_BRANCH" -- "$file"
    fi
done <<< "$MODIFIED_FILES"

# Process deleted files
echo -e "${GREEN}Processing deleted files...${NC}"
while IFS= read -r file; do
    if [[ -n "$file" ]] && ! should_exclude "$file"; then
        echo "  Deleting: $file"
        git rm -f "$file" 2>/dev/null || rm -f "$file"
    fi
done <<< "$DELETED_FILES"

# Show status
echo ""
echo -e "${YELLOW}Current status:${NC}"
git status --short

echo ""
echo -e "${GREEN}Selective merge complete!${NC}"
echo "Review the changes and commit when ready." 