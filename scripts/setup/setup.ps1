# setup.ps1 - Windows Setup Script for Cursor LaTeX Zotero Template

# Run with elevated privileges if needed
if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
    Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

# Function to check if command exists
function Test-CommandExists {
    param ($command)
    $oldPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Stop'
    try { Get-Command $command; return $true }
    catch { return $false }
    finally { $ErrorActionPreference = $oldPreference }
}

# Install Chocolatey if missing
if (!(Test-CommandExists choco)) {
    Write-Host "Installing Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
} else {
    Write-Host "Chocolatey already installed."
}

choco upgrade chocolatey -y

# Warn about MiKTeX installation
echo "Warning: Installing MiKTeX takes some time. Continue? [y/n]"
$confirm = Read-Host
if ($confirm -match '^([yY][eE][sS]|[yY])$') {
    choco install miktex -y
} else {
    Write-Host "Skipping MiKTeX installation."
}

# Install system dependencies
choco install sqlite -y  # For Zotero database access

# Install Python if missing (uv requires Python)
if (!(Test-CommandExists python)) {
    choco install python -y
}

# Install uv for Python package management
if (!(Test-CommandExists uv)) {
    Write-Host "Installing uv..."
    powershell.exe -c "irm https://github.com/astral-sh/uv/releases/latest/download/uv-install.ps1 | iex"
    $env:PATH += ";$env:USERPROFILE\.cargo\bin"
} else {
    Write-Host "uv already installed."
}

# Install Python dependencies
Write-Host "Installing Python dependencies..."
uv sync

# Install VS Code extensions if CLI available
$VSCODE_CLI = $null
if (Test-CommandExists cursor) {
    $VSCODE_CLI = "cursor"
} elseif (Test-CommandExists code) {
    $VSCODE_CLI = "code"
}

if ($VSCODE_CLI) {
    Write-Host "Installing VS Code extensions..."
    & $VSCODE_CLI --install-extension edwinkofler.vscode-hyperupcall-pack-latex
    & $VSCODE_CLI --install-extension notzaki.pandocciter
} else {
    Write-Host "VS Code/Cursor CLI not found. Please install extensions manually: edwinkofler.vscode-hyperupcall-pack-latex and notzaki.pandocciter"
}

Write-Host "Setup complete! Restart your terminal or PowerShell."
Write-Host "To run the Zotero sync: uv run python scripts/syncing/main.py"

# Note about Zotero path
Write-Host "Note: On Windows, update config.yaml with zotero_data_dir: '$env:APPDATA\Zotero\Zotero' if needed." 