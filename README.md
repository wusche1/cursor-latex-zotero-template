# Cursor + LaTeX + Zotero: Academic Writing Template with AI Assistance

This MVP template combines Cursor, LaTeX, and Zotero for efficient academic writing with AI-powered research assistance.

## Core Features

### 🤖 AI Assistant with Full Paper Access
- **Your AI assistant can read all your cited papers**: The sync script automatically extracts markdown versions of all papers in your Zotero collection
- **Fact-checking and verification**: AI can verify claims against the actual paper content, suggest relevant quotes, and ensure citation accuracy
- **Smart citation suggestions**: Type '@' in your notes for intelligent reference suggestions from your project-specific bibliography

### 📚 Seamless Zotero Integration
- **Auto-sync bibliography**: Papers added to your Zotero collection automatically sync to your project
- **Custom markdown extraction**: Special support for LessWrong posts and Alignment Forum articles - extracts clean markdown for AI reference
- **LaTeX label autocomplete**: Type '@' to get suggestions for both citations AND LaTeX labels (figures, sections, etc.) in your markdown notes

### ✍️ Optimized Writing Workflow
- **Two-stage writing process**: Write freely in `notes.md` files, then let AI transform into polished LaTeX chapters
- **Clear division of labor**: You provide the ideas and content in notes; AI helps structure and polish into LaTeX chapters
- **Version control friendly**: Clean separation of notes, LaTeX source, and references

## Quick Start
1. On GitHub, use this as a template: Click 'Use this template' > Name your repo (e.g., 'my-paper-title') > Create.
2. Clone your new repo: `git clone your-repo-url` (folder will match paper name).
3. Run setup scripts (macOS and Windows supported; assumes Cursor installed).

## Setup

### macOS
- **Dependencies**: `./scripts/setup.sh` (installs Homebrew if needed, MacTeX, Python via uv, etc.; confirm large downloads).
- **Zotero & Better BibTeX**: `./scripts/setup_zotero.sh` (installs if missing, downloads addon, prints GUI install/config steps; auto-creates collection matching repo name).

To make the scripts executable and run the installation:

```bash
chmod +x scripts/*.sh
./scripts/setup.sh
./scripts/setup_zotero.sh
```

### Windows
- **Dependencies**: `./scripts/setup.ps1` (installs Chocolatey if needed, MiKTeX, Python via uv, etc.; confirm large downloads).
- **Zotero**: Install manually from [zotero.org](https://www.zotero.org/download/) (automatic installation not available on Windows).

Run the setup script in PowerShell as Administrator:

```powershell
./scripts/setup.ps1
```

### Better BibTeX Setup (Both Platforms)
After running the setup scripts, you'll need to manually complete the Better BibTeX setup:
1. Open Zotero → Tools → Add-ons → Install Add-on From File (select the downloaded .xpi)
2. Restart Zotero
3. Go to Tools → Better BibTeX → Preferences → Set Citation key format to `[auth:lower][year]`
4. Enable auto-export: Edit → Preferences → Better BibTeX → Automatic export
5. Add your collection, set export as BibTeX to `bib/refs.bib` in your project
6. Enable 'Pin BibTeX key' for stable keys

## How It Works

1. **Write naturally**: Draft your ideas in `content/*/notes.md` files
2. **Add references**: Import papers to Zotero; they auto-sync to your project
3. **Let AI help**: Ask the assistant to transform notes into polished LaTeX chapters
4. **Verify accuracy**: AI can check citations against the actual paper content

Run the sync script while writing:

```bash
# Run once
uv run python scripts/main.py
```

AI assistants are pre-configured with this structure, workflow, and rules via `.cursor/rules/` in the repo.

## Feedback

We'd love to hear about your experience with this template! Please share any feedback, suggestions, or issues through our [feedback form](https://docs.google.com/forms/d/e/1FAIpQLSdBpFHVVR9a93MyGgg1wfH7u3CwEq58SfGXMzxy0N96AngMww/viewform?usp=dialog).

## Notes
- Supports macOS and Windows. For Linux, adapt the setup scripts manually.
- Rules: See `.cursor/rules/` for assistant behavior.
- Customize: Add sections in `content/`, update `main.tex` inputs. 