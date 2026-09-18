from app.graph.state import AgentState


def validate_answer(state: AgentState) -> dict[str, str]:
    answer = state.get("answer", "").strip()

    if not answer:
        return {
            "answer": (
                "I could not generate a reliable answer from "
                "the available information."
            )
        }

    answer_lower = answer.lower()

    prohibited_approval_phrases = [
        "dispute is approved",
        "dispute has been approved",
        "fee waiver is approved",
        "fee waiver has been approved",
        "request is approved",
        "request has been approved",
    ]

    if any(
        phrase in answer_lower
        for phrase in prohibited_approval_phrases
    ):
        return {
            "answer": (
                "The request may require additional review. "
                "Approval cannot be confirmed from the available information."
            )
        }

    return {
        "answer": answer
    }
