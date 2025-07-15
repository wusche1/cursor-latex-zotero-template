#!/bin/bash

# Check for required argument
if [ $# -eq 0 ]; then
  echo "Error: Please provide a PR title as argument."
  echo "Usage: $0 'My PR Title'"
  exit 1
fi

PR_TITLE="$1"

# Sanitize for branch name
BRANCH_NAME=$(echo "$PR_TITLE" | tr ' ' '-' | tr '[:upper:]' '[:lower:]')
TIMESTAMP=$(date +%s)
BRANCH="pr-$BRANCH_NAME-$TIMESTAMP"

# Ensure we're not on main
if [ "$(git branch --show-current)" = "main" ]; then
  echo "Error: Please switch to a feature branch first."
  exit 1
fi

# Create new branch
git checkout -b "$BRANCH"

# Stage all changes
git add .

# Unstage excluded folders
git reset bib/ || true
git reset figures/ || true
git reset content/ || true

# Check if there's anything to commit
if git diff --cached --quiet; then
  echo "No changes to commit outside excluded folders."
  git checkout -
  git branch -D "$BRANCH"
  exit 0
fi

# Commit
git commit -m "$PR_TITLE"

# Push
git push origin HEAD

# Create PR (assumes gh CLI installed)
if command -v gh &> /dev/null; then
  gh pr create --base main --title "$PR_TITLE" --body "Automatic PR: $PR_TITLE\n\nExcludes changes in bib/, figures/, and content/ folders."
else
  echo "gh CLI not found. Please install it and run: gh pr create --base main --title '$PR_TITLE' --body 'Automatic PR excluding content folders'"
fi