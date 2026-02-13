---
name: zotero
description: Manage Zotero library - list collections, list papers, add papers to collections. Requires ZOTERO_API_KEY env var.
allowed-tools: Bash
---

# Zotero Library Management

Manage your Zotero library via the API.

## Prerequisites

Set `ZOTERO_API_KEY` environment variable with a Zotero API key that has read/write access.
Get one at: https://www.zotero.org/settings/keys

## Scripts

### List Collections

```bash
.claude/skills/zotero/scripts/list-collections.sh
```

### List Papers in Collection

```bash
.claude/skills/zotero/scripts/list-papers.sh <collection-key-or-name>
```

### Add Papers to Collection

```bash
.claude/skills/zotero/scripts/add-to-collection.sh <collection-key-or-name> <item-key> [item-key...]
```

### Add arXiv Paper

```bash
python3 .claude/skills/zotero/scripts/add-paper.py <arxiv-url-or-id> [collection-name]
```

Adds a new paper from arXiv to your library with PDF. Accepts full URLs or just the arXiv ID (e.g., `2412.14093`).

### Add Paper with Manual Metadata

```bash
python3 .claude/skills/zotero/scripts/add-paper-manual.py \
  --pdf "URL_TO_PDF" \
  --title "Paper Title" \
  --authors "First Author, Second Author" \
  --year "2025" \
  [--url "URL_TO_PAPER_PAGE"] \
  [--abstract "Abstract text"] \
  [--type report|preprint|journalArticle|conferencePaper|webpage] \
  [--publisher "Institution Name"] \
  [--collection "collection-name"]
```

Adds a paper with manually specified metadata. Use for non-arXiv papers like system cards and technical reports.

### Delete Papers

```bash
.claude/skills/zotero/scripts/delete-paper.sh <item-key> [item-key...]
```

Permanently deletes papers from your Zotero library.
