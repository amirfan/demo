from abc import ABC, abstractmethod

from app.schemas import ChatCompletionRequest, ChatMessage


class ModelProvider(ABC):
    """Abstract model provider interface for multi-model routing."""

    @abstractmethod
    def chat(self, request: ChatCompletionRequest) -> ChatMessage:
        raise NotImplementedError


class MockProvider(ModelProvider):
    """Mock provider for local development and integration testing."""

    def chat(self, request: ChatCompletionRequest) -> ChatMessage:
        last_user_message = next(
            (m.content for m in reversed(request.messages) if m.role == "user"),
            "",
        )
        return ChatMessage(
            role="assistant",
            content=f"[mock:{request.model}] 已收到: {last_user_message}",
        )


def provider_factory(model_name: str) -> ModelProvider:
    # 可在这里根据模型名前缀选择不同 Provider（openai/azure/local 等）
    return MockProvider()
