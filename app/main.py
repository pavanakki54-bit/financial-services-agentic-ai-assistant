from fastapi import FastAPI

from app.graph.workflow import build_workflow
from app.models.schemas import ChatRequest, ChatResponse


app = FastAPI(
    title="Financial Services Agentic AI Assistant",
    version="1.0.0",
)

graph = build_workflow()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "financial-services-agentic-ai-assistant",
    }


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    state = {
        "session_id": req.session_id,
        "message": req.message,
        "route": "",
        "context": "",
        "sources": [],
        "answer": "",
    }

    result = graph.invoke(state)

    return ChatResponse(
        session_id=req.session_id,
        answer=result["answer"],
        sources=result.get("sources", []),
    )
