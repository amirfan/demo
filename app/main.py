from uuid import uuid4

from fastapi import FastAPI

from app.schemas import ChatCompletionChoice, ChatCompletionRequest, ChatCompletionResponse
from app.services import provider_factory

app = FastAPI(title="AI Platform Starter", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/chat/completions", response_model=ChatCompletionResponse)
def create_chat_completion(payload: ChatCompletionRequest) -> ChatCompletionResponse:
    provider = provider_factory(payload.model)
    assistant_message = provider.chat(payload)

    return ChatCompletionResponse(
        id=f"chatcmpl-{uuid4().hex[:12]}",
        model=payload.model,
        choices=[
            ChatCompletionChoice(
                index=0,
                message=assistant_message,
            )
        ],
    )
