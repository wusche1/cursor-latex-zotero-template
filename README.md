# Cursor + LaTeX + Zotero: Academic Writing Template with AI Assistance

This MVP template combines Cursor, LaTeX, and Zotero for efficient academic writing. It's ideal for researchers, students, or anyone producing scholarly content, with seamless bibliography sync and AI-optimized workflow. Repo name = paper name = Zotero collection.

## Quick Start
1. On GitHub, use this as a template: Click 'Use this template' > Name your repo (e.g., 'my-paper-title') > Create.
2. Clone your new repo: `git clone your-repo-url` (folder will match paper name).
3. Run setups (macOS only; assumes Cursor installed).

## Setup
- **Dependencies**: `./scripts/setup.sh` (installs Homebrew if needed, MacTeX, etc.; confirm large downloads).
- **Zotero & Better BibTeX**: `./scripts/setup_zotero.sh` (installs if missing, downloads addon, prints GUI install/config steps; auto-creates collection matching repo name). After running the script, you'll need to manually complete the Better BibTeX setup:
  1. Open Zotero → Tools → Add-ons → Install Add-on From File (select the downloaded .xpi)
  2. Restart Zotero
  3. Go to Tools → Better BibTeX → Preferences → Set Citation key format to `[auth:lower][year]`
  4. Enable auto-export: Edit → Preferences → Better BibTeX → Automatic export
  5. Add your collection, set export as BibTeX to `bib/refs.bib` in your project
  6. Enable 'Pin BibTeX key' for stable keys
- **Bib Sync**: Edit `./scripts/zotero_collection_sync.sh` if needed (e.g., adjust interval), then run it (daemon syncs to `bib/`).

To make the scripts executable and run the installation:

```bash
chmod +x scripts/*.sh
./scripts/setup.sh
./scripts/setup_zotero.sh
```

## Workflow
Import papers, LessWrong posts, or Alignment Forum articles into your Zotero collection effortlessly.

In `content/*/notes.md`, freely jot down your authentic ideas and thoughts. When citing, type '@' for intelligent suggestions from your project-specific Zotero references.

This setup is optimized for AI assistance: Keep `notes.md` as your personal space for raw, genuine content. Let AI transform it into polished `content/*/chapter.tex` files, handling structure and flow . For fine-grained control, edit the LaTeX directly.

The repo auto-syncs with your Zotero collection via `scripts/zotero_collection_sync.sh`, extracting Markdown from sources into `bib/` folders. AI can verify claims by accessing these extracts.

Run the sync script in the background while you work on the paper:

```bash
./scripts/zotero_collection_sync.sh &
```

AI assistants are pre-configured with this structure, workflow, and rules via `.cursor/rules/` in the repo.

## Notes
- Assumes macOS. For other OS, adapt manually.
- Rules: See `.cursor/rules/` for assistant behavior.
- Customize: Add sections in `content/`, update `main.tex` inputs. 