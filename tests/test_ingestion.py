from app.rag.ingestion import load_policy_documents


def test_load_policy_documents():
    documents = load_policy_documents()

    assert len(documents) >= 2

    sources = [document["source"] for document in documents]

    assert "dispute_policy.md" in sources
    assert "fee_policy.md" in sources

    for document in documents:
        assert document["text"].strip()
