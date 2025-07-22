#!/bin/bash

set -e

# Function to check if command exists
function command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install Homebrew if missing
if ! command_exists brew; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo "Homebrew already installed."
fi

brew update

# Warn about MacTeX
echo "Warning: Installing MacTeX takes a long time (large download). Continue? [y/n]"
read -r confirm
if [[ "$confirm" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    brew install --cask mactex-no-gui
else
    echo "Skipping MacTeX installation."
fi

# Install system dependencies
brew install sqlite  # For Zotero database access

# Install uv for Python package management
if ! command_exists uv; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
else
    echo "uv already installed."
fi

# Install Python dependencies
echo "Installing Python dependencies..."
uv sync

# Install VS Code extensions if CLI available
VSCODE_CLI=""
if command_exists cursor; then
    VSCODE_CLI="cursor"
elif command_exists code; then
    VSCODE_CLI="code"
fi

if [ -n "$VSCODE_CLI" ]; then
    echo "Installing VS Code extensions..."
    "$VSCODE_CLI" --install-extension edwinkofler.vscode-hyperupcall-pack-latex
    "$VSCODE_CLI" --install-extension notzaki.pandocciter
else
    echo "VS Code/Cursor CLI not found. Please install extensions manually: edwinkofler.vscode-hyperupcall-pack-latex and notzaki.pandocciter"
fi

echo "Setup complete! Restart your terminal."
echo "To run the Zotero sync: uv run python scripts/syncing/main.py" 