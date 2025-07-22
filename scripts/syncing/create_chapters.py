#!/usr/bin/env python3
"""
Create chapters from literature markdown files for RAG system.

For PDFs: Split by ## [number] headings into separate chapter files
For posts: Create single chapter file with post title as filename
Merge short chapters (< min_chars) with following subchapters
"""

import re
from pathlib import Path
from typing import List, Tuple, Dict
import yaml


def extract_title_from_markdown(content: str) -> str:
    """Extract the main title from markdown content (first # heading)"""
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('# ') and not line.startswith('## '):
            return line[2:].strip()
    return "Unknown Title"


def is_pdf_source(item_dir: Path) -> bool:
    """Check if the item is from a PDF by looking at metadata"""
    metadata_file = item_dir / '.metadata.txt'
    if metadata_file.exists():
        metadata_content = metadata_file.read_text(encoding='utf-8')
        # Look for PDF file existence in the directory
        pdf_files = list(item_dir.glob("*.pdf"))
        return len(pdf_files) > 0
    return False


def find_chapter_headings(content: str) -> List[Tuple[int, str, str]]:
    """
    Find chapter headings based on whitelist patterns in markdown content.
    Returns list of (position, heading_text, chapter_identifier)
    """
    headings = []
    lines = content.split('\n')
    current_pos = 0
    appendix_seen = False  # Track if we've seen an appendix section
    
    # Base patterns that always work
    base_patterns = [
        # ## ABSTRACT, ## ACKNOWLEDGMENTS, etc.
        r'^## +(ABSTRACT|ACKNOWLEDGMENTS?|CONCLUSION|REFERENCES?|INTRODUCTION|METHODOLOGY?|METHODS?|RESULTS?|DISCUSSION|LIMITATIONS?|FUTURE WORK)(?:\s|$)',
        
        # ## number word (e.g., ## 1 Introduction, ## 2.1 Methods)
        r'^## +(\d+(?:\.\d+)*)\s+(.+)$',
        
        # ## Appendix (standalone)
        r'^## +Appendix\s*$',
        
        # ## Appendix A Title (double # for appendix with letter and title)
        r'^## +Appendix +([A-Z](?:\.\d+)*)\s+(.+)$'
    ]
    
    # Patterns that only work after seeing appendix
    letter_patterns = [
        # ## Letter.number (e.g., ## B.1 CONFLICT VARIATIONS)
        r'^## +([A-Z](?:\.\d+)*)\s+(.+)$',
        
        # ## Letter TITLE (e.g., ## B EXTENDED SENSITIVITY ANALYSIS)
        r'^## +([A-Z])\s+([A-Z][A-Z\s]+)$',
    ]
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        matched = False
        
        # First check base patterns (always allowed)
        for pattern in base_patterns:
            match = re.match(pattern, line_stripped, re.IGNORECASE)
            if match:
                full_heading = line_stripped
                
                # Check if this is an appendix mention
                if 'Appendix' in pattern:
                    appendix_seen = True
                    if len(match.groups()) >= 2:
                        chapter_id = f"Appendix_{match.group(1)}_{match.group(2)}"
                    elif len(match.groups()) == 1:
                        chapter_id = f"Appendix_{match.group(1)}"
                    else:
                        # Standalone ## Appendix
                        chapter_id = "Appendix"
                elif len(match.groups()) >= 2:
                    # Has number and title
                    chapter_id = f"{match.group(1)}_{match.group(2)}"
                elif len(match.groups()) == 1:
                    # Just number or single word
                    chapter_id = match.group(1)
                else:
                    # Fallback
                    chapter_id = line_stripped.replace('##', '').replace('#', '').strip()
                
                # Clean up chapter_id
                chapter_id = re.sub(r'[^\w\s-]', '', chapter_id)
                chapter_id = re.sub(r'\s+', '_', chapter_id)
                
                headings.append((current_pos, full_heading, chapter_id))
                matched = True
                break
        
        # If not matched and appendix has been seen, check letter patterns
        if not matched and appendix_seen:
            for pattern in letter_patterns:
                match = re.match(pattern, line_stripped, re.IGNORECASE)
                if match:
                    full_heading = line_stripped
                    
                    if len(match.groups()) >= 2:
                        # Has letter and title
                        chapter_id = f"{match.group(1)}_{match.group(2)}"
                    elif len(match.groups()) == 1:
                        # Just letter
                        chapter_id = match.group(1)
                    else:
                        # Fallback
                        chapter_id = line_stripped.replace('##', '').replace('#', '').strip()
                    
                    # Clean up chapter_id
                    chapter_id = re.sub(r'[^\w\s-]', '', chapter_id)
                    chapter_id = re.sub(r'\s+', '_', chapter_id)
                    
                    headings.append((current_pos, full_heading, chapter_id))
                    break
        
        current_pos += len(line) + 1  # +1 for newline
    
    return headings


def split_into_chapters(content: str, min_chars: int = 100) -> List[Tuple[str, str]]:
    """
    Split markdown content into chapters based on ## headings.
    Merge short chapters with following subchapters.
    Returns list of (chapter_title, chapter_content) tuples.
    """
    headings = find_chapter_headings(content)
    
    if not headings:
        # No chapter headings found, return entire content as single chapter
        title = extract_title_from_markdown(content)
        return [(title, content)]
    
    chapters = []
    content_length = len(content)
    
    for i, (pos, heading, chapter_id) in enumerate(headings):
        # Find the end position (start of next chapter or end of content)
        if i + 1 < len(headings):
            end_pos = headings[i + 1][0]
        else:
            end_pos = content_length
        
        # Extract chapter content
        chapter_content = content[pos:end_pos].strip()
        
        # Clean up chapter title for filename
        clean_title = heading.replace('##', '').strip()
        clean_title = re.sub(r'[^\w\s-]', '', clean_title)  # Remove special chars
        clean_title = re.sub(r'\s+', '_', clean_title)  # Replace spaces with underscores
        
        chapters.append((clean_title, chapter_content))
    
    # Merge short chapters with following chapters
    merged_chapters = []
    i = 0
    
    while i < len(chapters):
        title, content = chapters[i]
        
        # Check if this chapter is too short and has a following chapter
        if len(content) < min_chars and i + 1 < len(chapters):
            next_title, next_content = chapters[i + 1]
            
            # Check if next chapter is a numbered subchapter, or just merge any short chapter
            current_num = extract_chapter_number(title)
            next_num = extract_chapter_number(next_title)
            
            # Merge if it's a numbered subchapter OR if the current chapter is just too short
            should_merge = False
            if current_num and next_num and is_subchapter(current_num, next_num):
                should_merge = True  # Numbered subchapter case
            elif len(content) < min_chars:
                should_merge = True  # Any short chapter case
            
            if should_merge:
                # Merge with next chapter
                merged_title = f"{title}_and_{next_title}"
                merged_content = content + "\n\n" + next_content
                merged_chapters.append((merged_title, merged_content))
                i += 2  # Skip next chapter since we merged it
                continue
        
        merged_chapters.append((title, content))
        i += 1
    
    return merged_chapters


def extract_chapter_number(title: str) -> str:
    """Extract chapter number from title (e.g., '4_1_Introduction' -> '4.1')"""
    match = re.match(r'^(\d+(?:[_\.]\d+)*)', title)
    return match.group(1).replace('_', '.') if match else ""


def is_subchapter(parent_num: str, child_num: str) -> bool:
    """Check if child_num is a subchapter of parent_num (e.g., '4' and '4.1')"""
    if not parent_num or not child_num:
        return False
    
    # Convert underscores to dots for comparison
    parent_parts = parent_num.replace('_', '.').split('.')
    child_parts = child_num.replace('_', '.').split('.')
    
    # Child should have more parts and start with parent parts
    if len(child_parts) <= len(parent_parts):
        return False
    
    return child_parts[:len(parent_parts)] == parent_parts


def create_chapters_for_item(item_dir: Path, min_chars: int = 100):
    """Create chapters folder and files for a single literature item"""
    # Find the fulltext markdown file
    fulltext_files = list(item_dir.glob("*_fulltext.md"))
    
    if not fulltext_files:
        print(f"  No fulltext markdown found in {item_dir.name}")
        return
    
    fulltext_file = fulltext_files[0]
    content = fulltext_file.read_text(encoding='utf-8')
    
    # Create chapters directory
    chapters_dir = item_dir / "chapters"
    chapters_dir.mkdir(exist_ok=True)
    
    # Determine if this is a PDF or post
    if is_pdf_source(item_dir):
        # Split PDF into chapters
        chapters = split_into_chapters(content, min_chars)
        print(f"  PDF: Created {len(chapters)} chapters for {item_dir.name}")
    else:
        # Single chapter for posts
        title = extract_title_from_markdown(content)
        clean_title = re.sub(r'[^\w\s-]', '', title)
        clean_title = re.sub(r'\s+', '_', clean_title)
        chapters = [(clean_title, content)]
        print(f"  Post: Created 1 chapter for {item_dir.name}")
    
    # Write chapter files
    for i, (chapter_title, chapter_content) in enumerate(chapters):
        # Ensure unique filename
        filename = f"{i+1:02d}_{chapter_title}.md"
        chapter_file = chapters_dir / filename
        
        chapter_file.write_text(chapter_content, encoding='utf-8')
    
    print(f"    Wrote {len(chapters)} chapter files to {chapters_dir}")


def create_chapters(config: dict):
    """Process all literature items in the bib directory using config"""
    bib_dir = Path(config.get('output_dir', '../bib'))
    min_chars = config.get('chapter_split', {}).get('min_chars', 100)
    
    print(f"Creating chapters from literature in: {bib_dir}")
    print(f"Minimum chapter size: {min_chars} characters")
    print()
    
    # Process each item directory
    processed = 0
    skipped = 0
    for item_dir in bib_dir.iterdir():
        if item_dir.is_dir() and not item_dir.name.startswith('.'):
            # Check if chapters folder already exists
            chapters_dir = item_dir / "chapters"
            if chapters_dir.exists():
                print(f"  Skipping {item_dir.name} - chapters folder already exists")
                skipped += 1
                continue
            
            try:
                create_chapters_for_item(item_dir, min_chars)
                processed += 1
            except Exception as e:
                print(f"  Error processing {item_dir.name}: {e}")
    
    print()
    print(f"Processed {processed} literature items")
    print(f"Skipped {skipped} items (chapters already exist)")


def main():
    """Main entry point for standalone testing"""
    config_path = Path(__file__).parent.parent / 'config.yaml'
    
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    else:
        config = {'output_dir': '../bib', 'chapter_split': {'min_chars': 100}}
    
    print(f'=== Chapter Creation (Standalone) ===')
    create_chapters(config)


if __name__ == '__main__':
    main() 