from app.agents.router import route_request


def make_state(message: str) -> dict:
    return {
        "session_id": "test-001",
        "message": message,
        "route": "",
        "context": "",
        "sources": [],
        "answer": "",
    }


def test_fee_policy_routes_to_rag():
    result = route_request(
        make_state("What is the fee waiver policy?")
    )
    assert result["route"] == "rag"


def test_transaction_id_routes_to_transaction():
    result = route_request(
        make_state("Show me transaction TXN-1002")
    )
    assert result["route"] == "transaction"


def test_dispute_question_routes_to_rag():
    result = route_request(
        make_state("How long do I have to dispute a transaction?")
    )
    assert result["route"] == "rag"


def test_general_message_routes_to_general():
    result = route_request(
        make_state("Hello, how are you?")
    )
    assert result["route"] == "general"
