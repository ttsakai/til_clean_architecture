import pytest

from flask_app import create_app
from flask_setting import TestConfig

@pytest.fixture(scope='function')
def app():
    yield create_app(TestConfig)