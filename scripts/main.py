#!/usr/bin/env python3
import time
import yaml
from pathlib import Path

from zotero_sync import sync_zotero
from label_sync import sync_labels


def main():
    # Load config
    config_path = Path(__file__).parent / 'config.yaml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    interval = config.get('check_interval', 30)
    
    while True:
        print("\n--- Zotero sync ---")
        sync_zotero(config)
        
        print("\n--- Label sync ---")
        sync_labels(config)
        
        print(f"\nWaiting {interval}s...")
        time.sleep(interval)


if __name__ == "__main__":
    main() 