from abc import ABCMeta
from speakit.vectorstores.base import VectorStore
from speakit.llms.base import LLM
from typing import Dict


class Singleton(ABCMeta, type):
    """Singleton metaclass for ensuring only one instance of a class exists.

    In Python, we can say that every class is an instance of the `type` metaclass.
    `type` serves as the metaclass for all Python classes. It defines how classes
    are created and provides default behavior.

    Creating a singleton class is typically achieved by modifying the `__new__` method
    of the `type` class. However, in Python, directly modifying the `__new__` method of
    `type` is not allowed.

    To implement the singleton pattern, we can create a custom metaclass. When classes
    inherit from this metaclass, they will share a common variable called `_instance`.
    This variable can be used to store the single instance of each class, making the
    classes behave as singletons.

    As additional context, when a class is created in Python, the `__call__` method of
    the metaclass is invoked. This method in turn calls the `__new__` method of the class,
    which handles the creation of the instance. After that, the `__init__` method of the
    class is called to initialize the instance. Considering this flow, if we want to implement
    special behavior or logic, such as the singleton pattern, we should focus on the `__call__`
    method of the metaclass. This is where we can customize the instantiation process and
    implement our desired functionality.

    References:
        1. https://github.com/geekan/MetaGPT
        2. https://github.com/gvariable/bugbuster (not public yet)
    """

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            # `__call__` invoke `__new__` and `__init__` of the cls, therefore return an instance of cls
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Registry(metaclass=Singleton):
    # TODO(gpl): docstring

    def __init__(self) -> None:
        self.ttss = {}
        self.srs = {}
        self.llms: Dict[str:LLM] = {}
        self.vectorstores: Dict[str:VectorStore] = {}

    def _raise_type_error(expect, got):
        raise TypeError(f"Expect {expect}, but got {got}")

    def register_tts(self, name: str = ""):
        raise NotImplementedError

    def register_sr(self, name: str = ""):
        raise NotImplementedError

    def register_llm(self, name: str = ""):
        def do_register(model: LLM):
            if issubclass(model, LLM):
                self.llms[name if name else getattr(model, "__name__")] = model
            else:
                self._raise_type_error(LLM, type(model))
        return do_register

    def register_vectorstore(self, name: str = ""):
        def do_register(model: VectorStore):
            if issubclass(model, VectorStore):
                self.vectorstores[name if name else getattr(model, "__name__")] = model
            else:
                self._raise_type_error(VectorStore, type(model))

        return do_register
