from app.rag.chunking import chunk_document, chunk_documents
from app.rag.ingestion import load_policy_documents


def test_chunk_single_document():
    document = {
        "source": "test_policy.md",
        "text": "A" * 1000,
    }

    chunks = chunk_document(
        document,
        chunk_size=500,
        overlap=100,
    )

    assert len(chunks) == 3
    assert chunks[0]["source"] == "test_policy.md"
    assert chunks[0]["start"] == 0
    assert chunks[1]["start"] == 400


def test_chunk_policy_documents():
    documents = load_policy_documents()

    chunks = chunk_documents(
        documents,
        chunk_size=500,
        overlap=100,
    )

    assert len(chunks) > len(documents)

    for chunk in chunks:
        assert chunk["text"].strip()
        assert chunk["source"].endswith(".md")
        assert "chunk_id" in chunk


def test_invalid_chunk_settings():
    document = {
        "source": "test.md",
        "text": "Example policy",
    }

    try:
        chunk_document(
            document,
            chunk_size=100,
            overlap=100,
        )
    except ValueError:
        assert True
    else:
        assert False
