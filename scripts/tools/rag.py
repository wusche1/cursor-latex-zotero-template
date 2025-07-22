#!/usr/bin/env python3
"""
RAG (Retrieval Augmented Generation) interface for literature embeddings

Shows detailed information including abstracts and chapter previews for search results.
Only shows abstract once per paper to avoid repetition.

Usage:
    python scripts/tools/rag.py "your query here"
    python scripts/tools/rag.py "your query here" 10
"""

import sys
from pathlib import Path
import yaml
# Add parent directory to path to import from syncing
sys.path.append(str(Path(__file__).parent.parent))
from syncing.embeddings import LiteratureEmbeddings


def read_abstract_from_metadata(paper_name: str, bib_dir: Path) -> str:
    """Read abstract from paper's metadata file"""
    metadata_file = bib_dir / paper_name / ".metadata.txt"
    if not metadata_file.exists():
        return "No abstract available"
    
    try:
        content = metadata_file.read_text(encoding='utf-8')
        for line in content.split('\n'):
            if line.startswith('Abstract: '):
                abstract = line[10:].strip()
                return abstract if abstract else "No abstract available"
        return "No abstract available"
    except Exception as e:
        return f"Error reading abstract: {e}"


def read_chapter_preview(paper_name: str, chapter_name: str, bib_dir: Path, max_chars: int = 5000) -> str:
    """Read first max_chars characters from a chapter file"""
    chapter_file = bib_dir / paper_name / "chapters" / f"{chapter_name}.md"
    if not chapter_file.exists():
        return "Chapter file not found"
    
    try:
        content = chapter_file.read_text(encoding='utf-8')
        if len(content) <= max_chars:
            return content
        else:
            return content[:max_chars] + "\n\n[... truncated ...]"
    except Exception as e:
        return f"Error reading chapter: {e}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/tools/rag.py 'query' [num_results]")
        print("Example: python scripts/tools/rag.py 'transformer attention' 10")
        return
    
    # Load config
    config_path = Path(__file__).parent.parent / 'config.yaml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Get RAG settings from config
    rag_config = config.get('tools', {}).get('rag', {})
    default_results = rag_config.get('default_results', 5)
    max_results = rag_config.get('max_results', 20)
    preview_chars = rag_config.get('preview_chars', 5000)
    
    # Get query from command line
    query = sys.argv[1]
    
    # Get number of results (use config default)
    num_results = default_results
    if len(sys.argv) >= 3:
        try:
            requested_results = int(sys.argv[2])
            if requested_results > max_results:
                print(f"Warning: Requested {requested_results} results, but max is {max_results}. Using {max_results}.")
                num_results = max_results
            else:
                num_results = requested_results
        except ValueError:
            print(f"Invalid number of results: {sys.argv[2]}, using default: {default_results}")
            num_results = default_results
    
    # Initialize embeddings and get bib directory
    project_root = Path(__file__).parent.parent.parent
    bib_dir_name = config.get('output_dir', 'bib')
    bib_dir = project_root / bib_dir_name
    embeddings = LiteratureEmbeddings(bib_dir=str(bib_dir))
    
    # Search
    print(f"🔍 RAG Search for: '{query}'")
    print(f"📊 Returning top {num_results} results with detailed previews\n")
    print("=" * 80)
    
    results = embeddings.search(query, top_k=num_results)
    
    if not results:
        print("❌ No results found.")
        return
    
    # Keep track of papers we've already shown abstracts for
    shown_abstracts = set()
    
    # Process results
    for i, (paper, chapter, score) in enumerate(results, 1):
        print(f"\n📄 Result {i}: {paper} - {chapter}")
        print(f"🎯 Relevance Score: {score:.3f}")
        print("-" * 60)
        
        # Show abstract only if we haven't shown it for this paper yet
        if paper not in shown_abstracts:
            print("📝 Abstract:")
            abstract = read_abstract_from_metadata(paper, bib_dir)
            print(f"   {abstract}")
            print()
            shown_abstracts.add(paper)
        else:
            print("📝 Abstract: (same paper as above)")
            print()
        
        # Show chapter preview
        print(f"📖 Chapter Preview ({chapter}):")
        chapter_preview = read_chapter_preview(paper, chapter, bib_dir, max_chars=preview_chars)
        
        # Indent the preview for better readability
        indented_preview = '\n'.join(f"   {line}" for line in chapter_preview.split('\n'))
        print(indented_preview)
        
        # Show file path
        file_path = bib_dir / paper / "chapters" / f"{chapter}.md"
        if file_path.exists():
            print(f"\n📁 File: {file_path.relative_to(project_root)}")
        
        if i < len(results):  # Don't print separator after last result
            print("\n" + "=" * 80)
    
    print(f"\n✅ Showed {len(results)} results from {len(shown_abstracts)} unique papers")


if __name__ == "__main__":
    main() 