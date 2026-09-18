from app.agents.validator import validate_answer


def make_state(answer: str) -> dict:
    return {
        "session_id": "test-001",
        "message": "Test message",
        "route": "rag",
        "context": "",
        "sources": [],
        "answer": answer,
    }


def test_safe_answer_is_preserved():
    result = validate_answer(
        make_state(
            "Eligible transaction disputes should be reported within 60 days."
        )
    )

    assert "60 days" in result["answer"]


def test_unsupported_approval_is_blocked():
    result = validate_answer(
        make_state("Your dispute has been approved.")
    )

    assert "Approval cannot be confirmed" in result["answer"]
    assert "approved" not in result["answer"].lower()


def test_empty_answer_gets_fallback():
    result = validate_answer(
        make_state("")
    )

    assert "could not generate a reliable answer" in result["answer"]
