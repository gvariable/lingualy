from speakit.llms import OpenAILLM
import asyncio
import pytest


@pytest.fixture(scope="session")
def openaillm():
    llm = OpenAILLM(
        system_message="You are an assistant",
        memory_window_size=3,
    )
    yield llm


def test_openai_llm(openaillm):
    resp = openaillm.chat("hello!")
    assert isinstance(resp, str)
    assert len(resp) > 0

    resp = openaillm.chat("hello again!")
    assert isinstance(resp, str)
    assert len(resp) > 0


@pytest.mark.asyncio
async def test_openai_llm_async(openaillm):
    tasks = [openaillm.achat("hello!"), openaillm.achat("hello again!")]

    results = await asyncio.gather(*tasks)
    assert all(map(lambda x: isinstance(x, str) and len(x) > 0, results))
