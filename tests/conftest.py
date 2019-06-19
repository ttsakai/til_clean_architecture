import pytest

from app.flask_app import create_app
from app.flask_config import TestConfig

@pytest.fixture(scope='function')
def app():
    yield create_app(TestConfig)

