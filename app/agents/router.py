from app.graph.state import AgentState


def route_request(state: AgentState) -> dict[str, str]:
    message = state["message"].lower()

    # Specific transaction lookup
    if "txn-" in message:
        return {"route": "transaction"}

    # Fee-waiver eligibility questions
    eligibility_keywords = [
        "eligible for a fee waiver",
        "fee waiver eligibility",
        "qualify for a fee waiver",
        "eligible for waiver",
        "qualify for waiver",
    ]

    if any(keyword in message for keyword in eligibility_keywords):
        return {"route": "eligibility"}

    # Policy / knowledge questions
    policy_keywords = [
        "policy",
        "dispute",
        "refund",
        "fee",
        "waiver",
        "unauthorized",
        "documents",
        "report",
    ]

    if any(keyword in message for keyword in policy_keywords):
        return {"route": "rag"}

    # Other transaction-related questions
    transaction_keywords = [
        "transaction",
        "merchant",
        "purchase",
    ]

    if any(keyword in message for keyword in transaction_keywords):
        return {"route": "transaction"}

    return {"route": "general"}
