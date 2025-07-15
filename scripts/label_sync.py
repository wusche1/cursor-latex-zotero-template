#!/usr/bin/env python3
import re
from pathlib import Path
from datetime import datetime


def sync_labels(config):
    """Extract all LaTeX labels and combine with refs.bib into a single file"""
    project_root = Path(__file__).parent.parent
    
    # First, read the existing refs.bib content
    refs_bib_path = project_root / "bib" / "refs.bib"
    refs_content = ""
    if refs_bib_path.exists():
        refs_content = refs_bib_path.read_text()
    
    # Find all .tex files
    tex_files = list(project_root.rglob('*.tex'))
    
    # Extract all \label{...} commands
    all_labels = []
    for tex_file in tex_files:
        try:
            content = tex_file.read_text()
            labels = re.findall(r'\\label\{([^}]+)\}', content)
            all_labels.extend(labels)
        except:
            pass
    
    # Remove duplicates and sort
    all_labels = sorted(set(all_labels))
    
    # Get output file from config (now .bib instead of .json)
    output_path = config.get('label_extraction', {}).get('output_file', 'bib/labels.bib')
    if output_path.endswith('.json'):
        output_path = output_path.replace('.json', '.bib')
    
    output_file = project_root / output_path
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Start with the refs.bib content
    bib_content = refs_content
    
    # Add separator and label entries
    bib_content += f"\n\n% ===== AUTO-GENERATED LATEX LABELS =====\n"
    bib_content += f"% Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    bib_content += f"% Total labels: {len(all_labels)}\n\n"
    
    for label in all_labels:
        # Create a fake BibTeX entry for each label
        # Using @misc type and adding fields to make it distinguishable
        bib_content += f"@misc{{{label},\n"
        bib_content += f"  title = {{LaTeX Label: {label}}},\n"
        bib_content += f"  note = {{Internal cross-reference}},\n"
        bib_content += f"  keywords = {{label}},\n"
        bib_content += f"  year = {{9999}}\n"  # Far future year to sort separately
        bib_content += f"}}\n\n"
    
    # Save to .bib file
    with open(output_file, 'w') as f:
        f.write(bib_content)
    
    print(f"Combined {refs_bib_path.name} + {len(all_labels)} labels -> {output_path}") 