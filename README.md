# Claude Code + LaTeX + Zotero + RAG: Academic Writing Template with AI Assistance

> **This is the `example-paper` branch.** It contains a complete example paper (satirical paperclip maximization) demonstrating how to use this template. See the `claude-code` branch for the clean template.

This template combines Claude Code, LaTeX, and Zotero for efficient academic writing with AI-powered research assistance.

## Core Features

### AI Assistant with Full Paper Access
- **Your AI assistant can read all your cited papers**: The sync script automatically extracts markdown versions of all papers in your Zotero collection
- **Intelligent literature search**: Built-in RAG system allows the assistant to search across your entire literature collection, finding which papers support specific facts or what your sources say about any topic
- **Fact-checking and verification**: AI can verify claims against the actual paper content, suggest relevant quotes, and ensure citation accuracy
- **Zotero management via skill**: Claude Code can add arXiv papers, manage collections, and search your library directly through the Zotero skill

### Seamless Zotero Integration
- **Auto-sync bibliography**: Papers added to your Zotero collection automatically sync to your project
- **Custom markdown extraction**: Special support for LessWrong posts and Alignment Forum articles - extracts clean markdown for AI reference
- **LaTeX label autocomplete**: VS Code PandocCiter provides suggestions for citations and LaTeX labels in your markdown notes

### Optimized Writing Workflow
- **Two-stage writing process**: Write freely in `notes.md` files, then let AI transform into polished LaTeX chapters
- **Clear division of labor**: You provide the ideas and content in notes; AI helps structure and polish into LaTeX chapters
- **Version control friendly**: Clean separation of notes, LaTeX source, and references

## Quick Start
1. On GitHub, use this as a template: Click 'Use this template' > Name your repo (e.g., 'my-paper-title') > Create.
2. Clone your new repo: `git clone your-repo-url` (folder will match paper name).
3. Run setup scripts (macOS and Windows supported).

## Setup

### macOS
- **Dependencies**: `./scripts/setup/setup.sh` (installs Homebrew if needed, MacTeX, Python via uv, etc.; confirm large downloads).
- **Zotero & Better BibTeX**: `./scripts/setup/setup_zotero.sh` (installs if missing, downloads addon, prints GUI install/config steps; auto-creates collection matching repo name).

To make the scripts executable and run the installation:

```bash
chmod +x scripts/setup/*.sh
./scripts/setup/setup.sh
./scripts/setup/setup_zotero.sh
```

### Windows
- **Dependencies**: `./scripts/setup/setup.ps1` (installs Chocolatey if needed, MiKTeX, Python via uv, etc.; confirm large downloads).
- **Zotero**: Install manually from [zotero.org](https://www.zotero.org/download/) (automatic installation not available on Windows).

Run the setup script in PowerShell as Administrator:

```powershell
./scripts/setup/setup.ps1
```

### Better BibTeX Setup (Both Platforms)
After running the setup scripts, you'll need to manually complete the Better BibTeX setup:
1. Open Zotero > Tools > Add-ons > Install Add-on From File (select the downloaded .xpi)
2. Restart Zotero
3. Go to Zotero > Settings > Better BibTeX > Set Citation key format to `auth.lower + year`
4. Add some sources to your collection (otherwise export won't work)
5. Right-click on your collection > Export Collection...
6. Choose format: Better BibTeX, enable 'Keep Updated', do NOT enable 'Export Files'
7. Click OK and save to `bib/refs.bib` in your project (overwrite when prompted)

### Zotero API (Optional)
To let Claude Code manage your Zotero library directly (add papers, manage collections):
1. Get an API key at: https://www.zotero.org/settings/keys
2. Set `ZOTERO_API_KEY` in your environment

## How It Works

1. **Write naturally**: Draft your ideas in `content/*/notes.md` files
2. **Add references**: Import papers to Zotero; they auto-sync to your project
3. **Let AI help**: Ask the assistant to transform notes into polished LaTeX chapters
4. **Verify accuracy**: AI can check citations against the actual paper content
5. **Search your literature**: Both you and the AI assistant can search across all your papers using the RAG system

Run the sync script while writing:

```bash
# Run in background
nohup uv run python scripts/syncing/main.py > /dev/null 2>&1 &
```

Search your literature collection manually:

```bash
# Search for specific topics or facts across all your papers
uv run python scripts/tools/rag.py "your search query"
```

AI assistant instructions are configured via `CLAUDE.md` and `.claude/` in the repo.

## Feedback

We'd love to hear about your experience with this template! Please share any feedback, suggestions, or issues through our [feedback form](https://docs.google.com/forms/d/e/1FAIpQLSdBpFHVVR9a93MyGgg1wfH7u3CwEq58SfGXMzxy0N96AngMww/viewform?usp=dialog).

## Notes
- Supports macOS and Windows. For Linux, adapt the setup scripts manually.
- Rules: See `CLAUDE.md` and `.claude/` for assistant behavior.
- Customize: Add sections in `content/`, update `main.tex` inputs.
