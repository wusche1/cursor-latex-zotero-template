#!/usr/bin/env python3
"""
Simple search interface for literature embeddings

Usage:
    python scripts/search_bib.py "your query here"
    python scripts/search_bib.py "your query here" 10
"""

import sys
from pathlib import Path
# Add parent directory to path to import from syncing
sys.path.append(str(Path(__file__).parent.parent))
from syncing.embeddings import LiteratureEmbeddings


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/search_bib.py 'query' [num_results]")
        print("Example: python scripts/search_bib.py 'transformer attention' 10")
        return
    
    # Get query from command line
    query = sys.argv[1]
    
    # Get number of results (default 5)
    num_results = 5
    if len(sys.argv) >= 3:
        try:
            num_results = int(sys.argv[2])
        except ValueError:
            print(f"Invalid number of results: {sys.argv[2]}")
            return
    
    # Initialize embeddings
    embeddings = LiteratureEmbeddings()
    
    # Search
    print(f"Searching for: '{query}'")
    print(f"Returning top {num_results} results\n")
    
    results = embeddings.search(query, top_k=num_results)
    
    if not results:
        print("No results found.")
        return
    
    # Print results
    print("Results:")
    print("-" * 60)
    for i, (paper, chapter, score) in enumerate(results, 1):
        print(f"{i}. {paper} - {chapter}")
        print(f"   Score: {score:.3f}")
        
        # Show file path
        file_path = Path(__file__).parent.parent.parent / "bib" / paper / "chapters" / f"{chapter}.md"
        if file_path.exists():
            print(f"   File: {file_path.relative_to(Path(__file__).parent.parent.parent)}")
        print()


if __name__ == "__main__":
    main() 