"""
embedding.py

Generates sentence embeddings for research paper summaries.
"""


class EmbeddingGenerator:
    """Generate vector embeddings using Sentence Transformers."""

    def __init__(self):
        self.model = None

    def _get_model(self):
        if self.model is None:
            try:
                from sentence_transformers import SentenceTransformer
            except Exception as exc:
                raise RuntimeError(
                    "Sentence Transformers could not be imported. Install the backend requirements and ensure torch is available."
                ) from exc

            self.model = SentenceTransformer("all-MiniLM-L6-v2")
        return self.model

    def generate(self, text: str) -> list[float]:
        """
        Generate embedding for text.
        """
        if not text:
            return []

        model = self._get_model()
        embedding = model.encode(text)

        return embedding.tolist()


embedding_generator = EmbeddingGenerator()