import pytest
from unittest import mock

# domain layer
from app.domain.user import User

# use case interactor
from app.use_case.user_list import UserList

# use case input port
from app.use_case.request_object import user_list_request_object as req

user_data = [
    User('hoge','hoge','hoge@example.com'),
    User('huga','huga','huga@example.com'),
    User('foge','foge','foge@example.com')
]

@pytest.mark.parametrize('domain_users',user_data)
def test_execute(domain_users):
    repository = mock.Mock()

    # only know repository interface that has list method
    repository.list.return_value = domain_users
    user_list = UserList(repository)

    request = req.UserListRequestObject()

    response = user_list.execute(request)

    assert bool(response) is True
    repository.list.assert_called_with()
    assert response.value == domain_users