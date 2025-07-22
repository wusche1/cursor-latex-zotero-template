#!/usr/bin/env python3
import time
import yaml
from pathlib import Path

from zotero_metadata_sync import sync_zotero_metadata
from text_extraction import extract_text
from label_sync import sync_labels
from create_chapters import create_chapters
from embeddings import create_embeddings


def main():
    # Load config
    config_path = Path(__file__).parent.parent / 'config.yaml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    interval = config.get('check_interval', 30)
    
    while True:
        print("\n--- Zotero metadata sync ---")
        sync_zotero_metadata(config)
        
        print("\n--- Text extraction ---")
        extract_text(config)
        
        print("\n--- Label sync ---")
        sync_labels(config)
        
        print("\n--- Chapter creation ---")
        create_chapters(config)
        
        print("\n--- Embeddings creation ---")
        create_embeddings(config)
        
        print(f"\nWaiting {interval}s...")
        time.sleep(interval)


if __name__ == "__main__":
    main() 