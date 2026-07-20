"""
analysis_agent.py

Main Analysis Agent.

Supports:

1. PDF Analysis (RAG)
2. Direct Text Analysis (Abstract Fallback)
"""

from agents.analysis_agent.parser import extract_text
from agents.analysis_agent.chunker import chunk_text

from agents.knowledge_agent.embedding import embedding_generator
from agents.knowledge_agent.vector_store import vector_store

from agents.rag_agent import rag_agent


class AnalysisAgent:
    """Runs the complete analysis pipeline."""

    def _analyze_text(self, title: str, text: str):

        if not text.strip():
            raise ValueError("No text available for analysis.")

        print("Chunking text...")

        chunks = chunk_text(text)

        print(f"Generated {len(chunks)} chunks.")

        vector_store.clear()

        print("Generating embeddings and indexing...")

        for index, chunk in enumerate(chunks):

            embedding = embedding_generator.generate(chunk)

            vector_store.store_chunk(
                chunk_id=f"{title}_{index}",
                chunk_text=chunk,
                embedding=embedding,
                metadata={
                    "paper": title,
                    "chunk": index
                }
            )

        print("Indexing complete.")

        print("Running RAG analysis...")

        result = rag_agent.analyze()

        return {
            "title": title,
            "summary": result.get("summary", ""),
            "methods": result.get("methods", []),
            "datasets": result.get("datasets", []),
            "metrics": result.get("metrics", []),
            "limitations": result.get("limitations", [])
        }

    def analyze(self, title: str, pdf_path: str):

        print("\nReading PDF...")

        text = extract_text(pdf_path)

        return self._analyze_text(
            title=title,
            text=text
        )

    def analyze_text(self, title: str, text: str):

        print("\nAnalyzing Abstract...")

        return self._analyze_text(
            title=title,
            text=text
        )


analysis_agent = AnalysisAgent()