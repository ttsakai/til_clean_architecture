import pytest
from app.domain.user import User
from app.use_case.user_list import UserList
from unittest import mock

@pytest.fixture
def domain_users():
    return [
        User('hoge','hoge','hoge@example.com'),
        User('huga','huga','huga@example.com'),
        User('foge','foge','foge@example.com')
    ]

def test_execute(domain_user):
    repository = mock.Mock()        
    repository.list.return_value = domain_users


    user_list = UserList(repository)
    result = user_list.execute()

    repository.list.assert_called_with()
    assert domain_users == result