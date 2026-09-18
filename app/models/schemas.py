from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    session_id: str = Field(
        min_length=1,
        description="Unique identifier for the conversation",
    )

    message: str = Field(
        min_length=1,
        description="User message sent to the AI assistant",
    )


class ChatResponse(BaseModel):
    session_id: str
    answer: str
    sources: list[str] = []
