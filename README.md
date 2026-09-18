# Financial Services Agentic AI Assistant

Production-style Agentic AI portfolio project demonstrating LangGraph routing, Retrieval-Augmented Generation (RAG), semantic retrieval, controlled tool execution, validation, and FastAPI for financial-services workflows.

> Independent portfolio project using synthetic data only.

## Key Capabilities

- LangGraph-based request routing
- Retrieval-Augmented Generation (RAG)
- Sentence Transformer embeddings
- Semantic policy retrieval
- Transaction lookup tool
- Fee-waiver eligibility tool
- Validation and guardrails
- FastAPI REST API
- Automated testing with Pytest
- Docker-ready packaging

## Architecture

User -> FastAPI -> LangGraph Router

Router -> RAG / Transaction Tool / Eligibility Tool / General Route

Specialized Route -> Validator -> Final API Response

## Technology Stack

Python 3.12, FastAPI, LangGraph, Pydantic, Sentence Transformers, NumPy, scikit-learn, Pytest, Docker, REST APIs.

## Example Questions

- How long do I have to dispute a transaction?
- Show me transaction TXN-1002
- Am I eligible for a fee waiver?

## API

Health endpoint:

    GET /health

Chat endpoint:

    POST /chat

Example request:

    {
      "session_id": "portfolio-demo",
      "message": "How long do I have to dispute a transaction?"
    }

Example response:

    {
      "session_id": "portfolio-demo",
      "answer": "Eligible transaction disputes should be reported within 60 days of the transaction appearing on the statement.",
      "sources": ["dispute_policy.md"]
    }

## Run Locally

    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload

Swagger UI:

    http://127.0.0.1:8000/docs

## Testing

    pytest -q

The project includes automated tests covering API behavior, routing, retrieval, tools, validation, and LangGraph workflow components.

## Docker

A Dockerfile is included for containerized execution.

    docker build -t financial-agentic-ai .
    docker run -p 8000:8000 financial-agentic-ai

Docker execution should be validated in an environment with Docker installed before production use.

## Responsible AI

The implementation demonstrates grounded policy responses, controlled deterministic tool execution, source attribution, validation before final responses, prevention of unsupported approval claims, and synthetic-data isolation.

## Future Production Extensions

Potential extensions include Amazon Bedrock or Azure OpenAI, hybrid retrieval and reranking, production vector databases, authentication and authorization, human-in-the-loop workflows, persistent LangGraph checkpoints, observability, LLM evaluation, and cloud deployment.

These are future extensions and are not represented as completed production capabilities.

## Disclaimer

This is an independent educational portfolio project. All policies, transactions, account scenarios, and business rules are synthetic.

The repository is not affiliated with any financial institution and contains no customer information, employer information, proprietary source code, internal documentation, or production credentials.
