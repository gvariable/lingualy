from elevenlabs import generate
from .base import TTS
from typing import Union, Iterator, Optional
import os


class ElevenLabsTTS(TTS):
    def __init__(
        self, voice: Optional[str] = "Bella", api_key: Optional[str] = None
    ) -> None:
        if api_key is None:
            api_key = os.environ.get("ELEVEN_API_KEY")

        self.api_key = api_key
        self.model = "eleven_monolingual_v1"
        self.voice = voice

    def generate(self, text: str) -> bytes:
        return generate(text=text, voice=self.voice, model=self.model)

    async def agenerate(self, text: str) -> bytes:
        # TODO: Wait for PR at https://github.com/elevenlabs/elevenlabs-python/pull/80 to be merged.
        raise NotImplementedError

    def stream(self, text: Union[Iterator[str], str]) -> Iterator[bytes]:
        return generate(text=text, voice=self.voice, model=self.model, stream=True)

    async def astream(self, text: Union[Iterator[str], str]) -> Iterator[bytes]:
        raise NotImplementedError
