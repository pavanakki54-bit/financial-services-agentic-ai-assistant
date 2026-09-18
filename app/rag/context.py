from app.rag.retrieval import retrieve_chunks


def build_rag_context(
    query: str,
    top_k: int = 3,
) -> dict:
    """
    Retrieve relevant policy chunks and build
    a context string for downstream RAG generation.
    """

    results = retrieve_chunks(
        query=query,
        top_k=top_k,
    )

    context_parts = []
    sources = []

    for result in results:
        source = result["source"]

        context_parts.append(
            f"[Source: {source}]\n{result['text']}"
        )

        if source not in sources:
            sources.append(source)

    context = "\n\n---\n\n".join(context_parts)

    return {
        "query": query,
        "context": context,
        "sources": sources,
        "results": results,
    }
