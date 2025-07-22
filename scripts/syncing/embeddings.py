#!/usr/bin/env python3
"""
Literature Embedding System using ChromaDB

Handles embedding of academic papers with chapter-based chunking and overlap.
"""

import re
from pathlib import Path
from typing import List, Tuple, Set
import chromadb
from sentence_transformers import SentenceTransformer


class LiteratureEmbeddings:
    """Manages embeddings for academic literature using ChromaDB"""
    
    def __init__(self, db_path="embeddings", model_name='all-mpnet-base-v2', bib_dir="bib"):
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(
            name="literature_chunks",
            embedding_function=None,  # Disable automatic embedding
            metadata={"hnsw:space": "cosine"}  # Use cosine similarity
        )
        self.model = SentenceTransformer(model_name)
        self.bib_dir = Path(bib_dir)
        print(f"Initialized with model: {model_name}")
    
    def add_paper(self, paper_id: str):
        """Add all chapters from a paper to the embedding database"""
        paper_dir = self.bib_dir / paper_id
        chapters_dir = paper_dir / "chapters"
        
        if not chapters_dir.exists():
            print(f"No chapters directory found for {paper_id}")
            return
        
        # Get all chapter files
        chapter_files = sorted(chapters_dir.glob("*.md"))
        if not chapter_files:
            print(f"No chapter files found for {paper_id}")
            return
        
        print(f"Processing {len(chapter_files)} chapters for {paper_id}")
        
        all_chunks = []
        all_embeddings = []
        all_ids = []
        all_metadata = []
        
        for chapter_file in chapter_files:
            chapter_name = chapter_file.stem  # e.g., "03_2_OUR_SETUP_and_21_KEY_ELEMENTS"
            
            with open(chapter_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Create chunks with overlap
            chunks = self._create_chunks_with_overlap(content)
            
            for i, chunk in enumerate(chunks):
                chunk_id = f"{paper_id}_{chapter_name}_chunk_{i}"
                all_chunks.append(chunk)
                all_ids.append(chunk_id)
                all_metadata.append({
                    "paper": paper_id,
                    "chapter": chapter_name
                })
        
        if not all_chunks:
            print(f"No content found in chapters for {paper_id}")
            return
        
        # Generate embeddings
        print(f"Generating embeddings for {len(all_chunks)} chunks...")
        all_embeddings = self.model.encode(all_chunks, show_progress_bar=True)
        
        # Add to ChromaDB
        self.collection.add(
            embeddings=all_embeddings.tolist(),
            documents=all_chunks,
            metadatas=all_metadata,
            ids=all_ids
        )
        
        print(f"Successfully added {len(all_chunks)} chunks for {paper_id}")
    
    def remove_paper(self, paper_id: str):
        """Remove all chunks from a paper"""
        try:
            self.collection.delete(where={"paper": paper_id})
            print(f"Successfully removed paper: {paper_id}")
        except Exception as e:
            print(f"Error removing paper {paper_id}: {e}")
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, str, float]]:
        """
        Search for similar chunks and return top 5 distinct paper+chapter combinations
        
        Returns:
            List of (paper, chapter, score) tuples
        """
        # Search with more results to ensure we get 5 distinct paper+chapter combinations
        search_k = min(top_k * 10, 50)  # Search more to filter duplicates
        
        # Generate query embedding ourselves
        query_embedding = self.model.encode([query])
        
        results = self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=search_k
        )
        
        if not results['metadatas'] or not results['metadatas'][0]:
            return []
        
        # Extract results and convert distances to similarity scores
        metadata_list = results['metadatas'][0]
        distances = results['distances'][0]
        
        # Convert distances to similarity scores (1 - distance for cosine)
        similarities = [1 - d for d in distances]
        
        # Group by paper+chapter and keep highest score for each combination
        paper_chapter_scores = {}
        for metadata, similarity in zip(metadata_list, similarities):
            paper = metadata["paper"]
            chapter = metadata["chapter"]
            key = (paper, chapter)
            
            # Keep the highest score for this paper+chapter combination
            if key not in paper_chapter_scores or similarity > paper_chapter_scores[key]:
                paper_chapter_scores[key] = similarity
        
        # Sort by score and return top 5 distinct combinations
        sorted_results = sorted(
            paper_chapter_scores.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:top_k]
        
        # Format as (paper, chapter, score) tuples
        return [(paper, chapter, score) for (paper, chapter), score in sorted_results]
    
    def _create_chunks_with_overlap(self, content: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """
        Split content into overlapping chunks
        
        Args:
            content: Text content to split
            chunk_size: Target size of each chunk in characters
            overlap: Number of characters to overlap between chunks
        
        Returns:
            List of text chunks with overlap
        """
        if len(content) <= chunk_size:
            return [content]
        
        chunks = []
        start = 0
        
        while start < len(content):
            # Calculate end position
            end = start + chunk_size
            
            # If this is not the last chunk, try to find a good break point
            if end < len(content):
                # Look for sentence endings near the end position
                break_candidates = []
                search_start = max(start + chunk_size - 100, start)  # Look in last 100 chars
                search_end = min(end + 100, len(content))  # Look in next 100 chars
                
                # Find sentence endings (., !, ?, \n\n)
                for i in range(search_start, search_end):
                    if content[i] in '.!?' and i + 1 < len(content) and content[i + 1] in ' \n':
                        break_candidates.append(i + 1)
                    elif i + 1 < len(content) and content[i:i+2] == '\n\n':
                        break_candidates.append(i + 2)
                
                # Use the break point closest to our target end
                if break_candidates:
                    end = min(break_candidates, key=lambda x: abs(x - end))
            
            # Extract chunk
            chunk = content[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            # Move start position (with overlap)
            if end >= len(content):
                break
            start = max(end - overlap, start + 1)  # Ensure we make progress
        
        return chunks
    
    def list_papers(self) -> Set[str]:
        """Get list of all papers in the database"""
        try:
            # Get all unique paper IDs
            all_metadata = self.collection.get()['metadatas']
            papers = {meta['paper'] for meta in all_metadata if 'paper' in meta}
            return papers
        except Exception as e:
            print(f"Error listing papers: {e}")
            return set()
    
    def get_paper_stats(self, paper_id: str) -> dict:
        """Get statistics for a specific paper"""
        try:
            results = self.collection.get(where={"paper": paper_id})
            if not results['metadatas']:
                return {"error": f"Paper {paper_id} not found"}
            
            chapters = set()
            chunk_count = len(results['metadatas'])
            
            for meta in results['metadatas']:
                if 'chapter' in meta:
                    chapters.add(meta['chapter'])
            
            return {
                "paper": paper_id,
                "total_chunks": chunk_count,
                "chapters": sorted(list(chapters)),
                "chapter_count": len(chapters)
            }
        except Exception as e:
            return {"error": f"Error getting stats for {paper_id}: {e}"}


def create_embeddings(config: dict):
    """Auto-embed all papers that aren't in the database yet using config"""
    # Get config values
    bib_dir = Path(config.get('output_dir', 'bib'))
    db_path = config.get('embeddings', {}).get('db_path', 'embeddings')
    model_name = config.get('embeddings', {}).get('model_name', 'all-mpnet-base-v2')
    
    embeddings = LiteratureEmbeddings(db_path=db_path, model_name=model_name, bib_dir=str(bib_dir))
    
    # Get papers already in database
    embedded_papers = embeddings.list_papers()
    
    # Find all available papers in bib/
    available_papers = []
    
    for paper_dir in bib_dir.iterdir():
        if paper_dir.is_dir():
            chapters_dir = paper_dir / "chapters"
            if chapters_dir.exists() and list(chapters_dir.glob("*.md")):
                available_papers.append(paper_dir.name)
    
    # Find papers that are embedded but no longer exist in bib/
    papers_to_remove = [paper for paper in embedded_papers if paper not in available_papers]
    
    # Remove embeddings for papers that no longer exist
    if papers_to_remove:
        print(f"\nRemoving embeddings for {len(papers_to_remove)} papers that no longer exist:")
        for paper in papers_to_remove:
            print(f"  Removing {paper}")
            embeddings.remove_paper(paper)
        print()
    
    # Find papers that need embedding
    papers_to_embed = [paper for paper in available_papers if paper not in embedded_papers]
    
    print(f"Found {len(available_papers)} papers with chapters:")
    for paper in sorted(available_papers):
        status = "✓ embedded" if paper in embedded_papers and paper not in papers_to_remove else "○ not embedded"
        chapters_dir = bib_dir / paper / "chapters"
        chapter_count = len(list(chapters_dir.glob("*.md")))
        print(f"  {status} {paper} ({chapter_count} chapters)")
    
    if papers_to_embed:
        print(f"\nEmbedding {len(papers_to_embed)} new papers...")
        for paper in papers_to_embed:
            print(f"\n--- Processing {paper} ---")
            embeddings.add_paper(paper)
        
        print(f"\n✅ Successfully embedded all papers!")
        print(f"Total papers in database: {len(embeddings.list_papers())}")
    else:
        print(f"\n✅ All papers are already embedded!")
        print(f"Total papers in database: {len(embedded_papers) - len(papers_to_remove)}")


def main():
    """Main entry point for standalone testing"""
    config_path = Path(__file__).parent.parent / 'config.yaml'
    
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    else:
        config = {
            'output_dir': 'bib',
            'embeddings': {
                'db_path': 'embeddings',
                'model_name': 'all-mpnet-base-v2'
            }
        }
    
    print(f'=== Embeddings Creation (Standalone) ===')
    create_embeddings(config)


if __name__ == "__main__":
    main() 