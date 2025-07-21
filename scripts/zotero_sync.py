import sqlite3
import time
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

import yaml
import fitz  # PyMuPDF
from bs4 import BeautifulSoup
from markdownify import markdownify as md
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


@dataclass
class Attachment:
    """Represents a Zotero attachment"""
    key: str
    path: str
    content_type: str
    title: Optional[str] = None


def extract_pdf_text(file_path: Path, folder_name: str) -> str:
    """Extract text from PDF file"""
    doc = fitz.open(str(file_path))
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    
    return f"""# Full Text: {folder_name}

Extracted: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Source: PDF
---

{text}"""


<<<<<<< HEAD
def extract_html_text(file_path: Path, folder_name: str, remove_base64_images: bool = True) -> str:
=======
def extract_html_text(file_path: Path, folder_name: str, prefer_json_ld: bool = True) -> str:
>>>>>>> 0a5e31d (python extraction for lw and alignment forum actually works)
    """General HTML text extraction"""
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Regular HTML to markdown conversion
    markdown_content = md(str(soup))
    
    # Remove base64-encoded images if configured
    if remove_base64_images:
        markdown_content = _remove_base64_images(markdown_content)
    
    return f"""# Full Text: {folder_name}

Extracted: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Source: HTML Snapshot
---

{markdown_content}"""


def _remove_base64_images(markdown_content: str) -> str:
    """Remove base64-encoded images from markdown content"""
    # Pattern to match markdown images with data: URIs
    # Matches: ![alt text](data:image/type;base64,...)
    base64_image_pattern = r'!\[([^\]]*)\]\(data:image/[^;]+;base64,[^)]+\)'
    
    # Replace base64 images with placeholder or remove entirely
    # Option 1: Replace with placeholder showing alt text
    def replace_with_placeholder(match):
        alt_text = match.group(1)
        if alt_text:
            return f"[Image: {alt_text}]"
        else:
            return "[Image]"
    
    # Option 2: Remove entirely (uncomment this line and comment above to use)
    # return re.sub(base64_image_pattern, '', markdown_content)
    
    return re.sub(base64_image_pattern, replace_with_placeholder, markdown_content)


def extract_lesswrong_text(file_path: Path, folder_name: str, remove_base64_images: bool = True) -> str:
    """Extract text from LessWrong-style HTML files (JSON-LD first, then specific selectors)"""
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Try JSON-LD first
    json_ld_scripts = soup.find_all('script', type='application/ld+json')
    for script in json_ld_scripts:
        try:
            data = json.loads(script.string)
            if isinstance(data, dict) and 'text' in data:
                text_soup = BeautifulSoup(data['text'], 'html.parser')
                title = data.get('headline', folder_name)
                author_data = data.get('author', 'Unknown')
                if isinstance(author_data, list) and author_data:
                    author = author_data[0].get('name', 'Unknown') if isinstance(author_data[0], dict) else 'Unknown'
                elif isinstance(author_data, dict):
                    author = author_data.get('name', 'Unknown')
                else:
                    author = 'Unknown'
                date = data.get('datePublished', datetime.now().strftime("%Y-%m-%d"))
                markdown_content = md(str(text_soup))
                
                # Remove base64-encoded images if configured
                if remove_base64_images:
                    markdown_content = _remove_base64_images(markdown_content)
                
                return f"""# Full Text: {folder_name}

Title: {title}
Author: {author}
Date: {date}
Extracted: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Source: HTML Snapshot (LessWrong JSON-LD)
---

{markdown_content}"""
        except Exception as e:
            print(f"Error extracting LessWrong text: {e}")
            return extract_html_text(file_path, folder_name, remove_base64_images)


def extract_lesswrong_text(file_path: Path, folder_name: str) -> str:
    """Extract text from LessWrong HTML files"""
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Try JSON-LD first
    json_ld_scripts = soup.find_all('script', type='application/ld+json')
    for script in json_ld_scripts:
        try:
            data = json.loads(script.string)
            if isinstance(data, dict) and 'text' in data:
                text_soup = BeautifulSoup(data['text'], 'html.parser')
                title = data.get('headline', folder_name)
                author_data = data.get('author', 'Unknown')
                if isinstance(author_data, list) and author_data:
                    author = author_data[0].get('name', 'Unknown') if isinstance(author_data[0], dict) else 'Unknown'
                elif isinstance(author_data, dict):
                    author = author_data.get('name', 'Unknown')
                else:
                    author = 'Unknown'
                date = data.get('datePublished', datetime.now().strftime("%Y-%m-%d"))
                return f"""# Full Text: {folder_name}

Title: {title}
Author: {author}
Date: {date}
Extracted: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Source: HTML Snapshot (LessWrong JSON-LD)
---

{md(str(text_soup))}"""
        except (json.JSONDecodeError, KeyError):
            continue
    
    # Fallback to HTML scraping
    print(f"  LessWrong JSON-LD extraction failed for {folder_name}, attempting HTML fallback")
    post_content = soup.select_one('.PostsPage-postContent')
    if post_content:
        # Extract title
        title_el = soup.select_one('.PostsPageTitle-root')
        title = title_el.get_text(strip=True) if title_el else folder_name
        
        # Try multiple author selectors
        author_selectors = [
            '.UsersNameDisplay-userName',
            '.PostsAuthors-author',
            '.UsersNameDisplay-displayName',
            '[itemprop="author"]'
        ]
        author = 'Unknown'
        for selector in author_selectors:
            author_el = soup.select_one(selector)
            if author_el:
                author = author_el.get_text(strip=True)
                break
        
        # Extract date
        date_selectors = [
            'time',
            '[itemprop="datePublished"]',
            '.PostsPageDate-date'
        ]
        date = datetime.now().strftime("%Y-%m-%d")
        for selector in date_selectors:
            date_el = soup.select_one(selector)
            if date_el:
                date = date_el.get('datetime') or date_el.get_text(strip=True)
                break
        
        markdown_text = md(str(post_content))
        return f"""# Full Text: {folder_name}

Title: {title}
Author: {author}
Date: {date}
Extracted: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Source: HTML Snapshot (LessWrong Fallback)
---

{markdown_text}"""
    
    # If both fail, fall back to general HTML
    print(f"  LessWrong HTML fallback also failed for {folder_name}, using general extraction")
    return extract_html_text(file_path, folder_name)


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
                    itemTypes.typeName
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
                WHERE collectionItems.collectionID = ?
                AND items.itemID NOT IN (SELECT itemID FROM deletedItems)
                AND itemTypes.typeName NOT IN ('attachment', 'note');
            """, (collection_id,))
            
            for row in cur:
                item_id, item_key, title, first_author, year, item_type = row
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
                    url=url
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


class ZoteroSync:
    """Main class for syncing Zotero collections"""
    
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
        self.remove_base64_images = self.config['extraction']['html']['remove_base64_images']
        self.lesswrong_sites = self.config['extraction']['html']['lesswrong_sites']
        
        self.output_dir.mkdir(exist_ok=True)
        self.db = ZoteroDatabase(self.zotero_data_dir)
    
    def sync_collection(self):
        """Sync the configured collection"""
        print(f'Starting sync for collection: {self.collection_name}')
        
        collection_id = self.db.get_collection_id(self.collection_name)
        if not collection_id:
            print(f'ERROR: Collection {self.collection_name} not found!')
            return
        
        items = self.db.get_collection_items(collection_id)
        
        for item in items:
            self._process_item(item)
        
        print('Sync completed')
    
    def _process_item(self, item: ZoteroItem):
        """Process a single Zotero item"""
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
        
        # Process attachments
        attachments = self.db.get_attachments(item.item_id)
        pdf_processed = False
        
        # Process PDFs first
        for attachment in attachments:
            if attachment.content_type == 'application/pdf' and not pdf_processed:
                if self._process_pdf_attachment(attachment, item):
                    pdf_processed = True
                    break
        
        # Process HTML if no PDF was found
        if not pdf_processed:
            for attachment in attachments:
                if attachment.content_type == 'text/html':
                    if self._process_html_attachment(attachment, item):
                        break
    
    def _process_pdf_attachment(self, attachment: Attachment, item: ZoteroItem) -> bool:
        """Process a PDF attachment"""
        pdf_file = self._find_attachment_file(attachment, 'pdf')
        if not pdf_file:
            return False
        
        item_dir = self.output_dir / item.citation_key
        pdf_dest = item_dir / f'{item.citation_key}.pdf'
        text_dest = item_dir / f'{item.citation_key}_fulltext.md'
        
        # Skip if both artifacts already exist
        if pdf_dest.exists() and text_dest.exists():
            print(f'  Skipping PDF (already exists): {item.citation_key}.pdf')
            return True
        
        # Copy PDF
        shutil.copy(pdf_file, pdf_dest)
        print(f'  Copied PDF: {item.citation_key}.pdf')
        
        # Extract text
        text = extract_pdf_text(pdf_file, item.citation_key)
        text_dest.write_text(text)
        print(f'  Extracted text: {item.citation_key}_fulltext.md')
        
        return True
    
    def _process_html_attachment(self, attachment: Attachment, item: ZoteroItem) -> bool:
        """Process an HTML attachment"""
        html_file = self._find_attachment_file(attachment, 'html')
        if not html_file:
            return False
        
        item_dir = self.output_dir / item.citation_key
        html_dest = item_dir / f'{item.citation_key}.html'
        text_dest = item_dir / f'{item.citation_key}_fulltext.md'
        
        # Skip if both artifacts already exist
        if html_dest.exists() and text_dest.exists():
            print(f'  Skipping HTML (already exists): {item.citation_key}.html')
            return True
        
        # Copy HTML
        import shutil
        shutil.copy(html_file, html_dest)
        print(f'  Copied HTML: {item.citation_key}.html')
        
<<<<<<< HEAD
        # Extract text - use LessWrong parser for configured sites
        if item.url and any(site in item.url for site in self.lesswrong_sites):
            text = extract_lesswrong_text(html_file, item.citation_key, self.remove_base64_images)
            print(f'  Extracted LessWrong content: {item.citation_key}_fulltext.md')
        else:
            text = extract_html_text(html_file, item.citation_key, self.remove_base64_images)
=======
        # Extract text - use LessWrong parser for LessWrong URLs
        if item.url and ('lesswrong.com' in item.url or 'alignmentforum.org' in item.url):
            text = extract_lesswrong_text(html_file, item.citation_key)
            print(f'  Extracted LessWrong content: {item.citation_key}_fulltext.md')
        else:
            text = extract_html_text(html_file, item.citation_key, self.prefer_json_ld)
>>>>>>> 0a5e31d (python extraction for lw and alignment forum actually works)
            print(f'  Extracted and converted HTML to markdown: {item.citation_key}_fulltext.md')
        
        text_dest.write_text(text)
        
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
    
def sync_zotero(config: dict):
    """Run a single Zotero sync with the given configuration"""
    # Create a temporary config file in memory for ZoteroSync
    # (since it expects a file path, we'll modify the class to accept config dict)
    syncer = ZoteroSync(config)
    syncer.sync_collection()


def main():
    """Main entry point for standalone testing"""
    config_path = Path(__file__).parent / 'config.yaml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    print(f'=== Zotero Collection Sync (Standalone) ===')
    sync_zotero(config)


if __name__ == '__main__':
    main() 