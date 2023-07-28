from vectorstores import VectorStore


class Registry:
    def __init__(self) -> None:
        self.tts = {}
        self.stt = {}
        self.llms = {}
        self.vectorstores = {}

    def register_tts(self, model, name=None):
        ...

    def register_stt(self, name, model):
        self.stt[name] = model

    def register_llm(self, name, model):
        self.llms[name] = model

    def register_vectorstore(self, name=None):
        def decorator(model):
            if isinstance(model, VectorStore):
                if name == None:
                    self.vectorstores[getattr(model, "__name__")] = model
            else:
                raise TypeError("Model must be of type VectorStore")

        return decorator
