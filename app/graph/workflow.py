import re

from langgraph.graph import END, START, StateGraph

from app.agents.router import route_request
from app.agents.validator import validate_answer
from app.graph.state import AgentState
from app.rag.generator import generate_rag_answer
from app.rag.local_generator import LocalGroundedGenerator
from app.tools.eligibility_tool import check_fee_waiver_eligibility
from app.tools.transaction_tool import get_transaction


def rag_node(state: AgentState) -> dict:
    generator = LocalGroundedGenerator()

    result = generate_rag_answer(
        question=state["message"],
        generator=generator,
        top_k=3,
    )

    return {
        "context": result["context"],
        "sources": result["sources"],
        "answer": result["answer"],
    }


def transaction_node(state: AgentState) -> dict[str, str]:
    message = state["message"]

    match = re.search(
        r"TXN-\d+",
        message,
        re.IGNORECASE,
    )

    if not match:
        return {
            "answer": "Please provide a transaction ID such as TXN-1002."
        }

    transaction_id = match.group().upper()
    transaction = get_transaction(transaction_id)

    if transaction is None:
        return {
            "answer": f"Transaction {transaction_id} was not found."
        }

    return {
        "answer": (
            f"Transaction {transaction_id}: "
            f"{transaction['merchant']}, "
            f"${transaction['amount']:.2f} "
            f"{transaction['currency']}, "
            f"status: {transaction['status']}, "
            f"category: {transaction['category']}."
        )
    }


def eligibility_node(state: AgentState) -> dict[str, str]:
    result = check_fee_waiver_eligibility(
        account_status="good_standing",
        previous_adjustments=0,
        reason_provided=True,
    )

    if result["eligible"]:
        answer = (
            "The request meets the preliminary fee-waiver "
            "eligibility criteria. Final approval is not guaranteed "
            "and requires review."
        )
    else:
        answer = (
            f"The request does not currently meet the preliminary "
            f"eligibility criteria. Reason: {result['reason']}"
        )

    return {
        "answer": answer
    }


def general_node(state: AgentState) -> dict[str, str]:
    return {
        "answer": "General node selected"
    }


def select_route(state: AgentState) -> str:
    return state["route"]


def build_workflow():
    workflow = StateGraph(AgentState)

    workflow.add_node("router", route_request)
    workflow.add_node("rag", rag_node)
    workflow.add_node("transaction", transaction_node)
    workflow.add_node("eligibility", eligibility_node)
    workflow.add_node("general", general_node)
    workflow.add_node("validator", validate_answer)

    workflow.add_edge(START, "router")

    workflow.add_conditional_edges(
        "router",
        select_route,
        {
            "rag": "rag",
            "transaction": "transaction",
            "eligibility": "eligibility",
            "general": "general",
        },
    )

    workflow.add_edge("rag", "validator")
    workflow.add_edge("transaction", "validator")
    workflow.add_edge("eligibility", "validator")
    workflow.add_edge("general", "validator")

    workflow.add_edge("validator", END)

    return workflow.compile()
