import pytest

from app.rag.prompt import build_rag_prompt


def test_build_rag_prompt():
    prompt = build_rag_prompt(
        question="How long do I have to dispute a transaction?",
        context=(
            "[Source: dispute_policy.md]\n"
            "Customers should report eligible disputes within 60 days."
        ),
    )

    assert "How long do I have to dispute a transaction?" in prompt
    assert "60 days" in prompt
    assert "using only" in prompt.lower()
    assert "do not invent facts" in prompt.lower()


def test_empty_question_rejected():
    with pytest.raises(ValueError):
        build_rag_prompt(
            question="",
            context="Example context",
        )


def test_empty_context_rejected():
    with pytest.raises(ValueError):
        build_rag_prompt(
            question="Example question",
            context="",
        )
