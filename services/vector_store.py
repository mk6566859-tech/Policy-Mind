import faiss
import numpy as np


class VectorStore:
    """FAISS index plus the chunk metadata associated with each vector."""

    def __init__(self):
        self.index = None
        self.documents = []

    def build(self, embeddings, documents: list[dict]):
        embeddings = np.asarray(embeddings, dtype="float32")
        if embeddings.ndim != 2 or len(embeddings) == 0:
            raise ValueError("No embeddings were provided.")

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)
        self.documents = documents

    def search(self, query_embedding, top_k: int = 5) -> list[dict]:
        if self.index is None:
            raise RuntimeError("The FAISS index has not been built.")

        query = np.asarray(query_embedding, dtype="float32")
        if query.ndim == 1:
            query = query.reshape(1, -1)

        k = min(top_k, len(self.documents))
        scores, indices = self.index.search(query, k)

        results = []
        for score, index in zip(scores[0], indices[0]):
            if index < 0:
                continue

            item = dict(self.documents[index])
            item["score"] = float(score)
            results.append(item)

        return results

    def clear(self):
        self.index = None
        self.documents = []
