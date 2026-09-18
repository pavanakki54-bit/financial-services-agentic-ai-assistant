from app.rag.context import build_rag_context


def test_dispute_context():
    rag = build_rag_context(
        "How long do I have to dispute a transaction?",
        top_k=3,
    )

    assert rag["query"]
    assert rag["context"]
    assert "dispute_policy.md" in rag["sources"]
    assert "60 days" in rag["context"]


def test_fee_context():
    rag = build_rag_context(
        "Can I request a fee waiver?",
        top_k=3,
    )

    assert rag["context"]
    assert "fee_policy.md" in rag["sources"]
