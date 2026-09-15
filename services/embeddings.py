from functools import lru_cache

from sentence_transformers import SentenceTransformer


@lru_cache(maxsize=1)
def get_embedding_model() -> SentenceTransformer:
    # Small, fast, strong general-purpose sentence embedding model.
    return SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts: list[str]):
    model = get_embedding_model()
    return model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    )
