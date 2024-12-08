from unittest.mock import MagicMock
from typing import List, Dict, Any
from pydantic_ai import Agent, RunContext
from chat.models import ChatResponse, ChatDependencies


class MockAgent(Agent[ChatDependencies, ChatResponse]):
    def __init__(self):
        super().__init__(
            model="test",
            deps_type=ChatDependencies,
            result_type=ChatResponse,
            system_prompt="Mock system prompt"
        )
        self.mock = MagicMock()
        self.mock.achat.return_value = ChatResponse(
            message="AI response",
            context_used=True,
            confidence=0.95
        )

    async def achat(
        self,
        message: str,
        history: List[Dict[str, Any]] = None,
        ctx: RunContext[ChatDependencies] = None
    ) -> ChatResponse:
        if message == "trigger_slow_response":
            raise TimeoutError("AI response timed out")
        return self.mock.achat(message, history)
