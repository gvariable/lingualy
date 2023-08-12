from abc import ABC, abstractclassmethod
from typing import Union, Iterator


class TTS(ABC):
    @abstractclassmethod
    def generate(self, text: Union[Iterator[str], str]) -> bytes:
        raise NotImplementedError

    @abstractclassmethod
    async def agenerate(self, text: Union[Iterator[str], str]) -> bytes:
        raise NotImplementedError

    @abstractclassmethod
    def stream(self, text: Union[Iterator[str], str]) -> Iterator[bytes]:
        raise NotImplementedError

    @abstractclassmethod
    async def astream(self, text: Union[Iterator[str], str]) -> Iterator[bytes]:
        raise NotImplementedError
