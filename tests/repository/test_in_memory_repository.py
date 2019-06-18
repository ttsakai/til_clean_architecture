import pytest 
from app.domain.user import User
from app.repository.in_memory_repository import InMemoryRepository
from unittest import mock


@pytest.fixture
def users_dict():
    return [
        {'user_id':'hoge','user_name':'hoge','email':'hoge@example.com'},
        {'user_id':'hoga','user_name':'hoga','email':'hoga@example.com'},
        {'user_id':'foge','user_name':'foge','email':'foge@example.com'},
    ]

def test_init_without_paramters(users_dict):
    repository = InMemoryRepository(users_dict)
    users = [ User.from_dict(user) for user in users_dict ]

    assert repository.list() == users