import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

import yaml
from docling.document_converter import DocumentConverter
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def safe_markdownify(html_content: str, max_recursion_depth: int = 100) -> str:
    """
    Safely convert HTML to markdown with recursion protection.
    
    Args:
        html_content: HTML string to convert
        max_recursion_depth: Maximum recursion depth to allow
    
    Returns:
        Markdown string, or error message if conversion fails
    """
    # Store original recursion limit
    original_limit = sys.getrecursionlimit()
    
    try:
        # Set a reasonable recursion limit
        sys.setrecursionlimit(max_recursion_depth)
        
        # Try to convert HTML to markdown
        markdown_content = md(html_content)
        return markdown_content
        
    except RecursionError as e:
        print(f"  WARNING: Recursion error during HTML to markdown conversion. Falling back to plain text extraction.")
        # Fall back to extracting just the text content
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup.get_text(separator='\n', strip=True)
        except Exception as fallback_error:
            return f"Failed to extract content due to recursion error.\nOriginal error: {str(e)}\nFallback error: {str(fallback_error)}"
    
    except Exception as e:
        print(f"  WARNING: Error during HTML to markdown conversion: {e}")
        # Fall back to extracting just the text content
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup.get_text(separator='\n', strip=True)
        except Exception as fallback_error:
            return f"Failed to extract content.\nOriginal error: {str(e)}\nFallback error: {str(fallback_error)}"
    
    finally:
        # Restore original recursion limit
        sys.setrecursionlimit(original_limit)


def extract_pdf_text(file_path: Path, folder_name: str) -> str:
    """Extract text from PDF file using Docling"""
    try:
        converter = DocumentConverter()
        result = converter.convert(str(file_path))
        markdown_content = result.document.export_to_markdown()
        return markdown_content
    except Exception as e:
        print(f"Error extracting PDF with Docling: {e}")
        return f"Failed to extract content from PDF.\nError: {str(e)}"


def extract_html_text(file_path: Path, folder_name: str, remove_base64_images: bool = True) -> str:
    """General HTML text extraction"""
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Regular HTML to markdown conversion with recursion protection
    markdown_content = safe_markdownify(str(soup))
    
    # Remove base64-encoded images if configured
    if remove_base64_images:
        markdown_content = _remove_base64_images(markdown_content)
    
    return markdown_content


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


def extract_lesswrong_text(file_path: Path, folder_name: str, remove_base64_images: bool = True) -> Tuple[str, dict]:
    """Extract text from LessWrong-style HTML files (JSON-LD first, then specific selectors)
    Returns tuple of (markdown_content, metadata_dict)"""
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
                markdown_content = safe_markdownify(str(text_soup))
                
                # Remove base64-encoded images if configured
                if remove_base64_images:
                    markdown_content = _remove_base64_images(markdown_content)
                
                # Return metadata separately
                metadata = {
                    'extracted_title': title,
                    'extracted_author': author,
                    'extracted_date': date
                }
                
                return markdown_content, metadata
        except Exception as e:
            print(f"Error extracting LessWrong text: {e}")
            return extract_html_text(file_path, folder_name, remove_base64_images), {}


class TextExtractor:
    """Main class for extracting text from PDF and HTML files"""
    
    def __init__(self, config):
        # Accept either a config dict or a file path
        if isinstance(config, dict):
            self.config = config
        else:
            with open(config, 'r') as f:
                self.config = yaml.safe_load(f)
        
        # Convert paths
        self.output_dir = Path(self.config['output_dir'])
        self.remove_base64_images = self.config['extraction']['html']['remove_base64_images']
        self.lesswrong_sites = self.config['extraction']['html']['lesswrong_sites']
    
    def extract_all(self):
        """Extract text from all items in the output directory"""
        print(f'Starting text extraction from: {self.output_dir}')
        
        processed = 0
        skipped = 0
        
        for item_dir in self.output_dir.iterdir():
            if item_dir.is_dir() and not item_dir.name.startswith('.'):
                if self._extract_item(item_dir):
                    processed += 1
                else:
                    skipped += 1
        
        print(f'Text extraction completed: {processed} processed, {skipped} skipped')
    
    def _extract_item(self, item_dir: Path) -> bool:
        """Extract text from a single item directory"""
        citation_key = item_dir.name
        text_dest = item_dir / f'{citation_key}_fulltext.md'
        metadata_path = item_dir / '.metadata.txt'
        
        # Skip if markdown already exists
        if text_dest.exists():
            print(f'  Skipping extraction (markdown already exists): {citation_key}_fulltext.md')
            return False
        
        # Look for PDF first
        pdf_files = list(item_dir.glob('*.pdf'))
        if pdf_files:
            pdf_file = pdf_files[0]
            print(f'  Extracting PDF text with Docling: {pdf_file.name} (this may take a while...)')
            text = extract_pdf_text(pdf_file, citation_key)
            text_dest.write_text(text, encoding='utf-8')
            print(f'  Extracted text: {citation_key}_fulltext.md')
            
            # Add extraction metadata
            if metadata_path.exists():
                with open(metadata_path, 'a') as f:
                    f.write(f'Extracted: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                    f.write(f'Extraction Method: PDF (via Docling)\n')
            
            return True
        
        # Look for HTML if no PDF
        html_files = list(item_dir.glob('*.html')) + list(item_dir.glob('*.htm'))
        if html_files:
            html_file = html_files[0]
            
            # Get URL from metadata for LessWrong detection
            url = None
            if metadata_path.exists():
                metadata_content = metadata_path.read_text()
                for line in metadata_content.split('\n'):
                    if line.startswith('URL: '):
                        url = line[5:].strip()
                        break
            
            # Extract text - use LessWrong parser for configured sites
            if url and any(site in url for site in self.lesswrong_sites):
                text, extra_metadata = extract_lesswrong_text(html_file, citation_key, self.remove_base64_images)
                print(f'  Extracted LessWrong content: {citation_key}_fulltext.md')
                extraction_method = "HTML (LessWrong JSON-LD)"
            else:
                text = extract_html_text(html_file, citation_key, self.remove_base64_images)
                extra_metadata = {}
                print(f'  Extracted and converted HTML to markdown: {citation_key}_fulltext.md')
                extraction_method = "HTML (Raw)"
            
            text_dest.write_text(text, encoding='utf-8')
            
            # Add extraction metadata
            if metadata_path.exists():
                with open(metadata_path, 'a') as f:
                    f.write(f'Extracted: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                    f.write(f'Extraction Method: {extraction_method}\n')
                    # Add extra metadata from LessWrong extraction if available
                    for key, value in extra_metadata.items():
                        f.write(f'{key.replace("_", " ").title()}: {value}\n')
            
            return True
        
        print(f'  No PDF or HTML files found for: {citation_key}')
        return False


def extract_text(config: dict):
    """Run text extraction with the given configuration"""
    extractor = TextExtractor(config)
    extractor.extract_all()


def main():
    """Main entry point for standalone testing"""
    config_path = Path(__file__).parent.parent / 'config.yaml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    print(f'=== Text Extraction (Standalone) ===')
    extract_text(config)


if __name__ == '__main__':
    main() 