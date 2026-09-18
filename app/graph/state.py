from typing import TypedDict


class AgentState(TypedDict):
    session_id: str
    message: str
    route: str
    context: str
    sources: list[str]
    answer: str
