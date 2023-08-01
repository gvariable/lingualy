from abc import ABC, abstractmethod
from typing import *
import langchain

from langchain.cache import InMemoryCache

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
