"""
retrieval_agent.py

Task-aware semantic retrieval for RAG.
"""

from agents.knowledge_agent.embedding import embedding_generator
from agents.knowledge_agent.vector_store import vector_store


class RetrievalAgent:

    def __init__(self):

        self.queries = {
            "summary": """
Summarize the research paper.
Focus on:
- abstract
- introduction
- conclusion
- overall contribution
""",

            "methods": """
Identify:
- methodology
- algorithms
- architecture
- framework
- techniques
- proposed approach
""",

            "datasets": """
Identify:
- datasets
- benchmark datasets
- corpus
- knowledge graph
- data source
""",

            "metrics": """
Identify:
- evaluation metrics
- accuracy
- precision
- recall
- F1
- BLEU
- ROUGE
- AUC
""",

            "limitations": """
Identify:
- limitations
- assumptions
- weaknesses
- future work
- open challenges
"""
        }

    def retrieve(self, query: str, top_k: int = 5):

        embedding = embedding_generator.generate(query)

        return vector_store.retrieve_chunks(
            query_embedding=embedding,
            top_k=top_k
        )

    def retrieve_all(self):

        merged = []

        seen = set()

        for task, query in self.queries.items():

            results = self.retrieve(query, top_k=5)

            documents = results["documents"]
            metadata = results["metadatas"]

            for doc, meta in zip(documents, metadata):

                if doc not in seen:

                    seen.add(doc)

                    merged.append(
                        {
                            "task": task,
                            "text": doc,
                            "metadata": meta
                        }
                    )

        # Prioritize chunks from the beginning/end of the paper
        merged.sort(
            key=lambda x: (
                x["metadata"].get("chunk", 999)
            )
        )

        return merged


retrieval_agent = RetrievalAgent()