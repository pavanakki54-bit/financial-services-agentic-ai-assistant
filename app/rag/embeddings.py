from functools import lru_cache

import numpy as np
from sentence_transformers import SentenceTransformer


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def get_embedding_model() -> SentenceTransformer:
    """
    Load and cache the embedding model.

    The model is loaded only once per Python process.
    """
    return SentenceTransformer(MODEL_NAME)


def embed_text(text: str) -> np.ndarray:
    """
    Convert one string into a normalized embedding vector.
    """
    if not text.strip():
        raise ValueError("text cannot be empty")

    model = get_embedding_model()

    embedding = model.encode(
        text,
        normalize_embeddings=True,
    )

    return np.asarray(embedding, dtype=np.float32)


def embed_texts(texts: list[str]) -> np.ndarray:
    """
    Convert multiple strings into normalized embedding vectors.
    """
    if not texts:
        raise ValueError("texts cannot be empty")

    if any(not text.strip() for text in texts):
        raise ValueError("texts cannot contain empty strings")

    model = get_embedding_model()

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
    )

    return np.asarray(embeddings, dtype=np.float32)
