import uuid
from speakit.llms import LLM


class Session:
    def __init__(self, llm: LLM) -> None:
        self.id = uuid.uuid4()
        self.llm = llm
        self.history = []

    def chat(self, query: str):
        response = self.llm.chat(query)
        self._update_history(query, response)
        return response

    async def achat(self, query: str):
        response = await self.llm.achat(query)
        self._update_history(query, response)
        return response

    def _update_history(self, query, response):
        self.history.append({"human": query, "bot": response})

    def persist(self):
        pass

    @classmethod
    def load(cls):
        pass
