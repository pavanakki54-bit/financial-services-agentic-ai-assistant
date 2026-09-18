from app.rag.generator import generate_rag_answer


class FakeGenerator:
    def generate(self, prompt: str) -> str:
        assert "Retrieved Context:" in prompt
        assert "User Question:" in prompt

        return (
            "Eligible transaction disputes should be reported "
            "within 60 days of appearing on the statement."
        )


def test_generate_rag_answer():
    result = generate_rag_answer(
        question="How long do I have to dispute a transaction?",
        generator=FakeGenerator(),
        top_k=3,
    )

    assert "60 days" in result["answer"]
    assert "dispute_policy.md" in result["sources"]
    assert result["context"]
