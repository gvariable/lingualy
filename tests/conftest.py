import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def env():
    load_dotenv(".env")
