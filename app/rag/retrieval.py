import numpy as np

from app.rag.chunking import chunk_documents
from app.rag.embeddings import embed_text, embed_texts
from app.rag.ingestion import load_policy_documents


def cosine_similarity(
    query_vector: np.ndarray,
    document_vectors: np.ndarray,
) -> np.ndarray:
    """
    Compute cosine similarity between one query vector
    and multiple document vectors.
    """

    query_norm = np.linalg.norm(query_vector)
    document_norms = np.linalg.norm(document_vectors, axis=1)

    denominator = document_norms * query_norm

    similarities = np.divide(
        document_vectors @ query_vector,
        denominator,
        out=np.zeros_like(document_norms),
        where=denominator != 0,
    )

    return similarities


def retrieve_chunks(
    query: str,
    top_k: int = 3,
) -> list[dict]:
    """
    Retrieve the most semantically relevant policy chunks.
    """

    if not query.strip():
        raise ValueError("query cannot be empty")

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    documents = load_policy_documents()
    chunks = chunk_documents(documents)

    chunk_texts = [chunk["text"] for chunk in chunks]

    chunk_embeddings = embed_texts(chunk_texts)
    query_embedding = embed_text(query)

    scores = cosine_similarity(
        query_vector=query_embedding,
        document_vectors=chunk_embeddings,
    )

    ranked_indices = np.argsort(scores)[::-1]

    results = []

    for index in ranked_indices[:top_k]:
        chunk = chunks[index].copy()
        chunk["score"] = float(scores[index])
        results.append(chunk)

    return results
