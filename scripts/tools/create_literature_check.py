#!/usr/bin/env python3
"""
Create literature_check folder structure with citation overview for each chapter.

This script:
1. Deletes and recreates the literature_check folder
2. Creates a subfolder for each content directory
3. Generates citations_overview.json files listing all citations with their line numbers
4. Spawns Cursor CLI agents to verify each citation and generate reports

Usage:
  uv run python scripts/tools/create_literature_check.py

Note: Currently in DEBUG mode - only spawns first 3 agents for testing.
"""

import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import List, Dict, Any


def extract_citations_from_tex(tex_file: Path) -> List[Dict[str, Any]]:
    r"""
    Extract all \cite{...} commands from a LaTeX file.
    
    Returns list of citation entries with:
    - citation_number: sequential number starting from 1
    - papers: list of citation keys
    - line: line number where citation appears
    - context: the line content for reference
    """
    citations = []
    
    if not tex_file.exists():
        return citations
    
    content = tex_file.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    # Pattern to match \cite commands with optional arguments
    # Matches: \cite{key1,key2}, \cite[text]{key}, \cite[pre][post]{key}
    cite_pattern = r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}'
    
    citation_counter = 1
    
    for line_num, line in enumerate(lines, start=1):
        # Find all citations in this line
        matches = re.finditer(cite_pattern, line)
        
        for match in matches:
            # Extract citation keys (may be comma-separated)
            keys_str = match.group(1)
            citation_keys = [key.strip() for key in keys_str.split(',')]
            
            citations.append({
                "citation_number": citation_counter,
                "papers": citation_keys,
                "line": line_num,
                "context": line.strip()
            })
            
            citation_counter += 1
    
    return citations


def create_literature_check_structure(workspace_root: Path):
    """
    Create literature_check folder structure with citation overviews.
    """
    lit_check_dir = workspace_root / "literature_check"
    content_dir = workspace_root / "content"
    
    # Step 1: Delete literature_check folder if it exists
    if lit_check_dir.exists():
        print(f"Deleting existing literature_check folder...")
        shutil.rmtree(lit_check_dir)
    
    # Step 2: Create literature_check folder
    lit_check_dir.mkdir(exist_ok=True)
    print(f"Created literature_check folder: {lit_check_dir}")
    
    # Step 3: Process each content subdirectory
    if not content_dir.exists():
        print(f"Warning: content directory not found at {content_dir}")
        return
    
    content_subdirs = sorted([d for d in content_dir.iterdir() if d.is_dir()])
    
    if not content_subdirs:
        print(f"Warning: no subdirectories found in {content_dir}")
        return
    
    print(f"\nProcessing {len(content_subdirs)} content directories...")
    
    for content_subdir in content_subdirs:
        # Create corresponding subfolder in literature_check
        check_subdir = lit_check_dir / content_subdir.name
        check_subdir.mkdir(exist_ok=True)
        
        # Find chapter.tex file
        chapter_tex = content_subdir / "chapter.tex"
        
        if not chapter_tex.exists():
            print(f"  {content_subdir.name}: No chapter.tex found, skipping")
            continue
        
        # Extract citations
        citations = extract_citations_from_tex(chapter_tex)
        
        # Create citations_overview.json
        json_file = check_subdir / "citations_overview.json"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(citations, f, indent=2, ensure_ascii=False)
        
        print(f"  {content_subdir.name}: Found {len(citations)} citations -> {json_file.relative_to(workspace_root)}")
    
    print(f"\n✓ Literature check structure created successfully!")


def spawn_citation_check_agent(
    workspace_root: Path,
    chapter_name: str,
    chapter_tex_path: Path,
    citation: Dict[str, Any],
    output_dir: Path
):
    """
    Spawn a Cursor CLI agent to check a single citation.
    
    Args:
        workspace_root: Root directory of the workspace
        chapter_name: Name of the chapter (e.g., "02_introduction")
        chapter_tex_path: Path to the chapter.tex file
        citation: Citation dict with citation_number, papers, line, context
        output_dir: Directory where report should be written
    """
    citation_num = citation["citation_number"]
    papers = citation["papers"]
    line_num = citation["line"]
    context = citation["context"]
    
    # Build the prompt for the agent
    prompt = f"""I need you to verify a citation in a LaTeX document.

**Citation Details:**
- Chapter: {chapter_name}
- File: {chapter_tex_path.relative_to(workspace_root)}
- Line number: {line_num}
- Line content: "{context}"
- Papers cited: {', '.join(papers)}

**Your Task:**
1. Read the chapter.tex file at the specified line to understand the citation in context
2. Read the fulltext markdown file(s) for the cited paper(s) from the bib/ directory
3. Verify whether the claims made in the citation are supported by the cited paper(s)
4. Write a report to: {output_dir.relative_to(workspace_root)}/report_{citation_num}.json

**Report Format:**
The report must be valid JSON with exactly these fields:
{{
  "report_text": "A short overview explaining whether the citation is correct and why",
  "report_rating": "one of: correct, incorrect, misleading, no_original, other"
}}

**Rating Definitions:**
- "correct": All claims are accurately supported by the cited paper(s)
- "incorrect": The cited information is NOT in the paper(s)
- "misleading": Information is technically in the paper but presented in a misleading way
- "no_original": Information is in the source paper, but the cited paper only references another paper with that info (not original)
- "other": None of the above categories apply

Please proceed with the verification and write the report.
"""
    
    # Spawn the cursor CLI agent
    try:
        result = subprocess.run(
            ["cursor-agent", "-p", prompt],
            cwd=workspace_root,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout per citation
        )
        
        print(f"    Citation {citation_num}: Agent spawned (papers: {', '.join(papers)})")
        
        if result.returncode != 0:
            print(f"      Warning: Agent returned non-zero exit code: {result.returncode}")
            if result.stderr:
                print(f"      Error: {result.stderr[:200]}")
    
    except subprocess.TimeoutExpired:
        print(f"    Citation {citation_num}: Agent timed out after 5 minutes")
    except FileNotFoundError:
        print(f"    Error: 'cursor-agent' CLI command not found. Please ensure Cursor CLI is installed.")
        return
    except Exception as e:
        print(f"    Citation {citation_num}: Error spawning agent: {e}")


def check_all_citations(workspace_root: Path, max_agents: int = None):
    """
    Spawn agents to check all citations in the literature_check structure.
    
    Args:
        workspace_root: Root directory of the workspace
        max_agents: Maximum number of agents to spawn (None = no limit)
    """
    lit_check_dir = workspace_root / "literature_check"
    content_dir = workspace_root / "content"
    
    if not lit_check_dir.exists():
        print("Error: literature_check directory does not exist.")
        return
    
    print("\n=== Spawning Citation Check Agents ===\n")
    
    if max_agents:
        print(f"DEBUG MODE: Only spawning first {max_agents} agents\n")
    
    total_citations = 0
    
    for check_subdir in sorted(lit_check_dir.iterdir()):
        if not check_subdir.is_dir():
            continue
        
        # Check if we've hit the limit
        if max_agents and total_citations >= max_agents:
            print(f"\nReached debug limit of {max_agents} agents. Stopping.")
            break
        
        chapter_name = check_subdir.name
        citations_file = check_subdir / "citations_overview.json"
        
        if not citations_file.exists():
            continue
        
        # Load citations
        with open(citations_file, 'r', encoding='utf-8') as f:
            citations = json.load(f)
        
        if not citations:
            continue
        
        print(f"Chapter {chapter_name}: Checking citations...")
        
        chapter_tex_path = content_dir / chapter_name / "chapter.tex"
        
        # Spawn an agent for each citation
        for citation in citations:
            # Check if we've hit the limit
            if max_agents and total_citations >= max_agents:
                break
            
            spawn_citation_check_agent(
                workspace_root,
                chapter_name,
                chapter_tex_path,
                citation,
                check_subdir
            )
            total_citations += 1
    
    print(f"\n✓ Spawned {total_citations} citation check agents")


def main():
    """Main entry point"""
    # Find workspace root (where this script is located)
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent.parent
    
    print("=== Creating Literature Check Structure ===\n")
    print(f"Workspace root: {workspace_root}")
    
    # Step 1: Create the literature_check structure
    create_literature_check_structure(workspace_root)
    
    # Step 2: Spawn agents to check citations (DEBUG: only first 3)
    check_all_citations(workspace_root, max_agents=3)


if __name__ == '__main__':
    main()

