import json
from unittest import mock
import pytest

from app.domain.user import User

user_dict = {'user_id':'hoge','user_name':'hoge','email':'hoge@example.com'}

user = User.from_dict(user_dict)
users = [user]

@mock.patch('app.use_case.user_list.UserList')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = users