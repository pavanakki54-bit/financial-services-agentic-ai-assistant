def build_rag_prompt(
    question: str,
    context: str,
) -> str:
    """
    Build a grounded prompt using the user's question
    and retrieved policy context.
    """

    if not question.strip():
        raise ValueError("question cannot be empty")

    if not context.strip():
        raise ValueError("context cannot be empty")

    return f"""
You are a financial-services policy assistant.

Answer the user's question using only the information
provided in the retrieved context.

Rules:
1. Do not invent facts.
2. Do not use information outside the provided context.
3. If the context does not contain enough information,
   say that the available policy information is insufficient.
4. Keep the answer concise and clear.
5. Do not claim that an action, dispute, waiver, or request
   has been approved.
6. Treat all information as synthetic portfolio data.

Retrieved Context:
{context}

User Question:
{question}

Answer:
""".strip()
