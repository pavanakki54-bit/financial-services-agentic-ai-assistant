from typing import Any


def chunk_document(
    document: dict[str, str],
    chunk_size: int = 500,
    overlap: int = 100,
) -> list[dict[str, Any]]:
    """
    Split one document into overlapping text chunks.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    text = document["text"]
    source = document["source"]

    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk_text = text[start:end].strip()

        if chunk_text:
            chunks.append(
                {
                    "chunk_id": f"{source}-{chunk_id}",
                    "source": source,
                    "text": chunk_text,
                    "start": start,
                    "end": end,
                }
            )

        if end == len(text):
            break

        start = end - overlap
        chunk_id += 1

    return chunks


def chunk_documents(
    documents: list[dict[str, str]],
    chunk_size: int = 500,
    overlap: int = 100,
) -> list[dict[str, Any]]:
    """
    Chunk multiple documents.
    """

    all_chunks = []

    for document in documents:
        all_chunks.extend(
            chunk_document(
                document=document,
                chunk_size=chunk_size,
                overlap=overlap,
            )
        )

    return all_chunks
