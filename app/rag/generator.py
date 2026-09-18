from typing import Protocol

from app.rag.context import build_rag_context
from app.rag.prompt import build_rag_prompt


class TextGenerator(Protocol):
    """
    Interface implemented by an LLM provider.
    """

    def generate(self, prompt: str) -> str:
        ...


def generate_rag_answer(
    question: str,
    generator: TextGenerator,
    top_k: int = 3,
) -> dict:
    """
    Retrieve context, construct the grounded prompt,
    call the text generator, and return the answer
    with source metadata.
    """

    rag = build_rag_context(
        query=question,
        top_k=top_k,
    )

    prompt = build_rag_prompt(
        question=question,
        context=rag["context"],
    )

    answer = generator.generate(prompt)

    return {
        "answer": answer,
        "sources": rag["sources"],
        "context": rag["context"],
    }
