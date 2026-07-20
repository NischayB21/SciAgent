"""
rag_agent.py

Retrieval-Augmented Generation Agent.
"""

from agents.retrieval_agent import retrieval_agent
from agents.analysis_agent.llm_extractor import extract_with_llm


class RAGAgent:
    """Uses retrieved chunks as context for the LLM."""

    def analyze(self):

        retrieved_chunks = retrieval_agent.retrieve_all()

        if not retrieved_chunks:
            return {
                "summary": "",
                "methods": [],
                "datasets": [],
                "metrics": [],
                "limitations": []
            }

        # Keep only the best 5 retrieved chunks
        retrieved_chunks = retrieved_chunks[:5]

        context = "\n\n".join(
            chunk["text"] for chunk in retrieved_chunks
        )

        print(f"Retrieved {len(retrieved_chunks)} chunks for LLM.")
        print(f"Context length: {len(context)} characters")

        return extract_with_llm(context)


rag_agent = RAGAgent()