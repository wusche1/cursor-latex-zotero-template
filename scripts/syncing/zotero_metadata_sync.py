import sqlite3
import time
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

import yaml
import shutil

@dataclass
class ZoteroItem:
    """Represents a Zotero library item"""
    item_id: int
    item_key: str
    citation_key: str
    title: str
    first_author: str
    year: str
    item_type: str
    url: Optional[str] = None
    abstract: Optional[str] = None


@dataclass
class Attachment:
    """Represents a Zotero attachment"""
    key: str
    path: str
    content_type: str
    title: Optional[str] = None


class ZoteroDatabase:
    """Handles all Zotero database operations"""
    
    def __init__(self, zotero_data_dir: Path):
        self.zotero_db = zotero_data_dir / "zotero.sqlite"
        self.bbt_db = zotero_data_dir / "better-bibtex.sqlite"
    
    def get_collection_id(self, collection_name: str) -> Optional[int]:
        """Get collection ID from collection name"""
        with sqlite3.connect(f'file:{self.zotero_db}?immutable=1', uri=True) as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT collectionID FROM collections 
                WHERE collectionName = ? 
                AND collectionID NOT IN (SELECT collectionID FROM deletedCollections);
            """, (collection_name,))
            result = cur.fetchone()
            return result[0] if result else None
    
    def get_collection_items(self, collection_id: int) -> List[ZoteroItem]:
        """Get all items in a collection"""
        items = []
        
        with sqlite3.connect(f'file:{self.zotero_db}?immutable=1', uri=True) as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT DISTINCT
                    items.itemID,
                    items.key,
                    COALESCE(itemDataValues.value, 'Untitled') as title,
                    COALESCE(creators.lastName, 'Unknown') as firstAuthor,
                    COALESCE(SUBSTR(date.value, 1, 4), 'NoDate') as year,
                    itemTypes.typeName,
                    COALESCE(abstractValues.value, '') as abstract
                FROM items
                JOIN collectionItems ON items.itemID = collectionItems.itemID
                JOIN itemTypes ON items.itemTypeID = itemTypes.itemTypeID
                LEFT JOIN itemData AS titleData ON items.itemID = titleData.itemID 
                    AND titleData.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'title')
                LEFT JOIN itemDataValues ON titleData.valueID = itemDataValues.valueID
                LEFT JOIN itemCreators ON items.itemID = itemCreators.itemID AND itemCreators.orderIndex = 0
                LEFT JOIN creators ON itemCreators.creatorID = creators.creatorID
                LEFT JOIN itemData AS dateData ON items.itemID = dateData.itemID 
                    AND dateData.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'date')
                LEFT JOIN itemDataValues AS date ON dateData.valueID = date.valueID
                LEFT JOIN itemData AS abstractData ON items.itemID = abstractData.itemID 
                    AND abstractData.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'abstractNote')
                LEFT JOIN itemDataValues AS abstractValues ON abstractData.valueID = abstractValues.valueID
                WHERE collectionItems.collectionID = ?
                AND items.itemID NOT IN (SELECT itemID FROM deletedItems)
                AND itemTypes.typeName NOT IN ('attachment', 'note');
            """, (collection_id,))
            
            for row in cur:
                item_id, item_key, title, first_author, year, item_type, abstract = row
                citation_key = self._get_citation_key(item_key)
                url = self._get_item_url(conn, item_id)
                
                items.append(ZoteroItem(
                    item_id=item_id,
                    item_key=item_key,
                    citation_key=citation_key,
                    title=title,
                    first_author=first_author,
                    year=year,
                    item_type=item_type,
                    url=url,
                    abstract=abstract if abstract else None
                ))
        
        return items
    
    def _get_citation_key(self, item_key: str) -> str:
        """Get citation key from Better BibTeX"""
        if self.bbt_db.exists():
            with sqlite3.connect(f'file:{self.bbt_db}?immutable=1', uri=True) as conn:
                cur = conn.cursor()
                cur.execute("SELECT citationKey FROM citationkey WHERE itemKey = ?;", (item_key,))
                result = cur.fetchone()
                if result:
                    return result[0]
        return item_key
    
    def _get_item_url(self, conn: sqlite3.Connection, item_id: int) -> Optional[str]:
        """Get URL for an item"""
        cur = conn.cursor()
        cur.execute("""
            SELECT value FROM itemDataValues 
            WHERE valueID = (SELECT valueID FROM itemData 
                             WHERE itemID = ? AND fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'url'));
        """, (item_id,))
        result = cur.fetchone()
        return result[0] if result else None
    
    def get_attachments(self, item_id: int) -> List[Attachment]:
        """Get all attachments for an item"""
        attachments = []
        
        with sqlite3.connect(f'file:{self.zotero_db}?immutable=1', uri=True) as conn:
            cur = conn.cursor()
            
            # Get PDFs
            cur.execute("""
                SELECT 
                    items.key,
                    COALESCE(itemAttachments.path, '') as path
                FROM items
                JOIN itemAttachments ON items.itemID = itemAttachments.itemID
                WHERE itemAttachments.parentItemID = ?
                AND items.itemID NOT IN (SELECT itemID FROM deletedItems)
                AND itemAttachments.contentType = 'application/pdf';
            """, (item_id,))
            
            for key, path in cur:
                attachments.append(Attachment(key=key, path=path, content_type='application/pdf'))
            
            # Get HTML snapshots
            cur.execute("""
                SELECT 
                    items.key,
                    COALESCE(itemAttachments.path, '') as path,
                    COALESCE(titleValues.value, 'Snapshot') as title
                FROM items
                JOIN itemAttachments ON items.itemID = itemAttachments.itemID
                LEFT JOIN itemData AS titleData ON items.itemID = titleData.itemID 
                    AND titleData.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'title')
                LEFT JOIN itemDataValues AS titleValues ON titleData.valueID = titleValues.valueID
                WHERE itemAttachments.parentItemID = ?
                AND items.itemID NOT IN (SELECT itemID FROM deletedItems)
                AND itemAttachments.contentType = 'text/html';
            """, (item_id,))
            
            for key, path, title in cur:
                attachments.append(Attachment(key=key, path=path, content_type='text/html', title=title))
        
        return attachments


class ZoteroMetadataSync:
    """Main class for syncing Zotero metadata and files (without extraction)"""
    
    def __init__(self, config):
        # Accept either a config dict or a file path
        if isinstance(config, dict):
            self.config = config
        else:
            with open(config, 'r') as f:
                self.config = yaml.safe_load(f)
        
        # Convert paths
        self.output_dir = Path(self.config['output_dir'])
        self.zotero_data_dir = Path(self.config['zotero_data_dir']).expanduser()
        self.collection_name = self.config.get('collection_name') or Path.cwd().name
        
        self.output_dir.mkdir(exist_ok=True)
        self.db = ZoteroDatabase(self.zotero_data_dir)
    
    def sync_collection(self):
        """Sync the configured collection metadata and files"""
        print(f'Starting metadata sync for collection: {self.collection_name}')
        
        collection_id = self.db.get_collection_id(self.collection_name)
        if not collection_id:
            print(f'ERROR: Collection {self.collection_name} not found!')
            return
        
        items = self.db.get_collection_items(collection_id)
        
        for item in items:
            self._process_item(item)
        
        print('Metadata sync completed')
    
    def _process_item(self, item: ZoteroItem):
        """Process a single Zotero item - metadata and file copying only"""
        item_dir = self.output_dir / item.citation_key
        item_dir.mkdir(exist_ok=True)
        
        # Save metadata
        metadata_path = item_dir / '.metadata.txt'
        with open(metadata_path, 'w') as f:
            f.write(f'Title: {item.title}\n')
            f.write(f'Author: {item.first_author}\n')
            f.write(f'Year: {item.year}\n')
            f.write(f'Type: {item.item_type}\n')
            f.write(f'Citation Key: {item.citation_key}\n')
            f.write(f'Zotero Key: {item.item_key}\n')
            if item.url:
                f.write(f'URL: {item.url}\n')
            if item.abstract:
                f.write(f'Abstract: {item.abstract}\n')
        
        # Process attachments - copy files only
        attachments = self.db.get_attachments(item.item_id)
        pdf_processed = False
        
        # Process PDFs first
        for attachment in attachments:
            if attachment.content_type == 'application/pdf' and not pdf_processed:
                if self._copy_pdf_attachment(attachment, item):
                    pdf_processed = True
                    break
        
        # Process HTML if no PDF was found
        if not pdf_processed:
            for attachment in attachments:
                if attachment.content_type == 'text/html':
                    if self._copy_html_attachment(attachment, item):
                        break
    
    def _copy_pdf_attachment(self, attachment: Attachment, item: ZoteroItem) -> bool:
        """Copy a PDF attachment without extraction"""
        pdf_file = self._find_attachment_file(attachment, 'pdf')
        if not pdf_file:
            return False
        
        item_dir = self.output_dir / item.citation_key
        pdf_dest = item_dir / f'{item.citation_key}.pdf'
        
        # Copy PDF if it doesn't exist
        if not pdf_dest.exists():
            shutil.copy(pdf_file, pdf_dest)
            print(f'  Copied PDF: {item.citation_key}.pdf')
        else:
            print(f'  PDF already exists: {item.citation_key}.pdf')
        
        return True
    
    def _copy_html_attachment(self, attachment: Attachment, item: ZoteroItem) -> bool:
        """Copy an HTML attachment without extraction"""
        html_file = self._find_attachment_file(attachment, 'html')
        if not html_file:
            return False
        
        item_dir = self.output_dir / item.citation_key
        html_dest = item_dir / f'{item.citation_key}.html'
        
        # Copy HTML if it doesn't exist
        if not html_dest.exists():
            shutil.copy(html_file, html_dest)
            print(f'  Copied HTML: {item.citation_key}.html')
        else:
            print(f'  HTML already exists: {item.citation_key}.html')
        
        return True
    
    def _find_attachment_file(self, attachment: Attachment, file_type: str) -> Optional[Path]:
        """Find the actual file for an attachment"""
        zotero_storage = self.zotero_data_dir / 'storage' / attachment.key
        
        if attachment.path.startswith('storage:'):
            file_path = zotero_storage / attachment.path[8:]
            if file_path.exists():
                return file_path
        elif attachment.path:
            file_path = Path(attachment.path)
            if file_path.exists():
                return file_path
        
        # Look for files in storage directory
        if zotero_storage.exists():
            if file_type == 'pdf':
                pdf_files = list(zotero_storage.glob('*.pdf'))
                if pdf_files:
                    return pdf_files[0]
            elif file_type == 'html':
                for ext in ['*.html', '*.htm']:
                    html_files = list(zotero_storage.glob(ext))
                    if html_files:
                        return html_files[0]
        
        return None


def sync_zotero_metadata(config: dict):
    """Run a single Zotero metadata sync with the given configuration"""
    syncer = ZoteroMetadataSync(config)
    syncer.sync_collection()


def main():
    """Main entry point for standalone testing"""
    config_path = Path(__file__).parent.parent / 'config.yaml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    print(f'=== Zotero Metadata Sync (Standalone) ===')
    sync_zotero_metadata(config)


if __name__ == '__main__':
    main() 