#!/usr/bin/env python3
"""
Simple search interface for literature embeddings

Usage:
    python scripts/search_bib.py "your query here"
    python scripts/search_bib.py "your query here" 10
"""

import sys
from pathlib import Path
import yaml
# Add parent directory to path to import from syncing
sys.path.append(str(Path(__file__).parent.parent))
from syncing.embeddings import LiteratureEmbeddings


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/search_bib.py 'query' [num_results]")
        print("Example: python scripts/search_bib.py 'transformer attention' 10")
        return
    
    # Load config
    config_path = Path(__file__).parent.parent / 'config.yaml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Get search settings from config
    search_config = config.get('tools', {}).get('search', {})
    default_results = search_config.get('default_results', 5)
    max_results = search_config.get('max_results', 50)
    
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
    
    # Initialize embeddings
    bib_dir = config.get('output_dir', 'bib')
    project_root = Path(__file__).parent.parent.parent
    embeddings = LiteratureEmbeddings(bib_dir=str(project_root / bib_dir))
    
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
        file_path = project_root / bib_dir / paper / "chapters" / f"{chapter}.md"
        if file_path.exists():
            print(f"   File: {file_path.relative_to(project_root)}")
        print()


if __name__ == "__main__":
    main() 