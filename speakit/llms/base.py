from abc import ABC, abstractmethod
from typing import *
from typing import Any

import langchain
from langchain.cache import InMemoryCache
from langchain.callbacks.base import AsyncCallbackHandler, BaseCallbackHandler

# TODO(gpl): make it configurable, and if it is enabled, asking the same question will result in the same answer.
langchain.llm_cache = InMemoryCache()


class LLM(ABC):
    def __init__(self, callbacks: List, memory_window_size: int = 5) -> None:
        ...

    @abstractmethod
    def chat(self):
        ...

    @abstractmethod
    async def achat(self):
        ...


def stream_handler(token: str, **kwargs):
    ...


class StreamCallbackHandler(BaseCallbackHandler):
    def __init__(self) -> None:
        pass

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        # TODO: notify the client that a new token is available
        ...

    def on_llm_end(self, *args, **kwargs) -> Any:
        ...


class AsyncStreamCallbackHandler(AsyncCallbackHandler):
    ...
