# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an example paper demonstrating the Claude Code + LaTeX + Zotero template with RAG-based literature search capabilities. The example topic is a satirical paperclip maximization paper.

## Build Commands

```bash
# Compile LaTeX document (mirrors VS Code LaTeX Workshop pipeline)
# Output goes to ./output directory. TeX binaries are at /Library/TeX/texbin/
/Library/TeX/texbin/pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=./output main.tex && \
/Library/TeX/texbin/biber --output-directory=./output main && \
/Library/TeX/texbin/pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=./output main.tex && \
/Library/TeX/texbin/pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=./output main.tex

# Run Zotero sync daemon (extracts papers, creates embeddings)
uv run python scripts/syncing/main.py

# Search literature with RAG (returns chapter previews and abstracts)
uv run python scripts/tools/rag.py "your query"

# Simple bibliography search (returns file paths only)
uv run python scripts/tools/search_bib.py "your query"
```

## Architecture

### Content Structure
- `content/*/notes.md` - User's draft notes and source material
- `content/*/chapter.tex` - Polished LaTeX chapters (AI writes these from notes)
- `content/*/claude_notes.md` - AI's research notes for that chapter (only use when explicitly instructed to look something up and take notes)
- `main.tex` - Document root that includes all chapters

### Bibliography System
- `bib/refs.bib` - BibTeX file auto-synced from Zotero
- `bib/labels.bib` - Extracted LaTeX labels for autocomplete
- `bib/[citation_key]/` - Per-paper folders containing:
  - `[key]_fulltext.md` - Complete paper text for AI reference
  - `chapters/*.md` - Paper split into searchable chapters
  - `.metadata.txt` - Paper metadata including abstract

### Sync Pipeline (`scripts/syncing/main.py`)
Runs continuously (30s interval) via nohup in the background. Check if it's running with `pgrep -f syncing/main.py`. If not running, start it with:
```bash
nohup uv run python scripts/syncing/main.py > /dev/null 2>&1 &
```

The pipeline executes:
1. `zotero_metadata_sync.py` - Syncs Zotero collection metadata
2. `text_extraction.py` - Extracts text from PDFs/HTML to markdown
3. `label_sync.py` - Extracts LaTeX labels to `labels.bib`
4. `create_chapters.py` - Splits papers into chapters for RAG
5. `embeddings.py` - Creates ChromaDB embeddings for search

### Experiments
- `experiments/` - Cloned experiment repositories (git-ignored). Clone relevant repos here to give the AI access to raw experiment code and results.

### Configuration
`scripts/config.yaml` controls Zotero sync, text extraction, chapter splitting, and embeddings settings.

## Key Rules

1. **Never modify `_fulltext.md` files** - Read-only source material
2. **Only write `chapter.tex` when explicitly asked** - User writes notes, AI transforms to LaTeX
3. **Put each sentence on a new line** in LaTeX files (improves diffs, invisible in PDF)
4. **Read existing chapters before editing** to maintain context and consistency
5. **Verify citations** by reading the corresponding `bib/[key]/[key]_fulltext.md`
6. **Use RAG tool** for literature questions: `uv run python scripts/tools/rag.py "query"`
7. **Notes are the source of truth** - chapters should never contain information not in notes
8. **Never manually edit `bib/refs.bib`** - This file is auto-synced from Zotero. To add citations, use the Zotero skill to add papers. The sync script will automatically update refs.bib.
9. **Avoid em-dashes (---)** - Overused by LLMs; use commas, parentheses, or separate sentences instead
