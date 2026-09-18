from app.graph.workflow import build_workflow


def make_state(message: str) -> dict:
    return {
        "session_id": "test-001",
        "message": message,
        "route": "",
        "context": "",
        "sources": [],
        "answer": "",
    }


def test_transaction_workflow():
    graph = build_workflow()

    result = graph.invoke(
        make_state("Show me transaction TXN-1002")
    )

    assert result["route"] == "transaction"
    assert "TXN-1002" in result["answer"]
    assert "Northstar Electronics" in result["answer"]
    assert "249.99" in result["answer"]


def test_unknown_transaction():
    graph = build_workflow()

    result = graph.invoke(
        make_state("Show me transaction TXN-9999")
    )

    assert result["route"] == "transaction"
    assert "not found" in result["answer"].lower()


def test_general_workflow():
    graph = build_workflow()

    result = graph.invoke(
        make_state("Hello, how are you?")
    )

    assert result["route"] == "general"
    assert result["answer"] == "General node selected"


def test_rag_workflow_retrieves_dispute_policy():
    graph = build_workflow()

    result = graph.invoke(
        make_state("How long do I have to dispute a transaction?")
    )

    assert result["route"] == "rag"
    assert "dispute_policy.md" in result["sources"]
    assert "60 days" in result["context"]
    assert result["context"]


def test_fee_policy_rag_workflow():
    graph = build_workflow()

    result = graph.invoke(
        make_state("What is the fee waiver policy?")
    )

    assert result["route"] == "rag"
    assert "fee_policy.md" in result["sources"]
    assert result["context"]
