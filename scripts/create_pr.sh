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
ORIGINAL_BRANCH=$(git branch --show-current)
if [ "$ORIGINAL_BRANCH" = "main" ]; then
  echo "Error: Please switch to a feature branch first."
  exit 1
fi

# Commit all changes on current branch to not lose them
if ! git diff --quiet || ! git diff --cached --quiet; then
  git add .
  git commit -m "$PR_TITLE"
  HAD_CHANGES=true
else
  HAD_CHANGES=false
fi

# Switch to main and create new branch
git checkout main
git checkout -b "$BRANCH"

# If there were changes, cherry-pick them without committing
if $HAD_CHANGES; then
  git cherry-pick -n "$ORIGINAL_BRANCH"
  git add .
  git reset HEAD bib/ || true
  git reset HEAD figures/ || true
  git reset HEAD content/ || true
fi

# Check if there's anything to commit
if git diff --cached --quiet; then
  echo "No changes to commit outside excluded folders."
  git checkout "$ORIGINAL_BRANCH"
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

# Switch back to original branch
git checkout "$ORIGINAL_BRANCH"