from speakit.utils import Registry
from speakit.llms.base import LLM

@Registry().register_llm()
class LLM1(LLM):
    pass

@Registry().register_llm()
class LLM2(LLM):
    pass

def test_singleton():
    assert id(Registry()) == id(Registry())

def test_registry():
    print(Registry().llms)
    assert len(Registry().llms) == 2