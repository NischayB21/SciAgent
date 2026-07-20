"""
vector_store.py

Stores and retrieves chunk embeddings using ChromaDB.
"""

import chromadb

# Persistent database
client = chromadb.PersistentClient(path="data/embeddings")

# Collection for research paper chunks
collection = client.get_or_create_collection(
    name="research_chunks"
)


class VectorStore:
    """Handles storage and retrieval of chunk embeddings."""

    def store_chunk(
        self,
        chunk_id: str,
        chunk_text: str,
        embedding: list[float],
        metadata: dict
    ):
        """
        Store a chunk and its embedding.
        """

        try:
            collection.add(
                ids=[chunk_id],
                documents=[chunk_text],
                embeddings=[embedding],
                metadatas=[metadata]
            )

        except Exception:
            # Ignore duplicate IDs during repeated testing
            pass

    def retrieve_chunks(
        self,
        query_embedding: list[float],
        top_k: int = 5
    ):
        """
        Retrieve the most semantically similar chunks.
        """

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        return {
            "documents": results.get("documents", [[]])[0],
            "metadatas": results.get("metadatas", [[]])[0],
            "distances": results.get("distances", [[]])[0]
        }

    def clear(self):
        """
        Remove all chunks from the vector database.
        Useful during testing.
        """

        data = collection.get()

        ids = data.get("ids", [])

        if ids:
            collection.delete(ids=ids)

        print("ChromaDB cleared.")

    def count(self):
        """
        Return the number of indexed chunks.
        """

        data = collection.get()

        return len(data.get("ids", []))


vector_store = VectorStore()