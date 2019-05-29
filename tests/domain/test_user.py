import pytest
import uuid
from app.domain.user import User


user_input = {
    'user_id': uuid.uuid4(),
    'user_name':'hoge',
    'email':'hoge@example.com',
}


def test_init():
    user = User(**user_input)

    assert user.user_id == user_input['user_id']
    assert user.user_name == user_input['user_name']
    assert user.email == user_input['email']


def test_from_dict():
    user = User.from_dict(user_input)

    assert user.user_id == user_input['user_id']
    assert user.user_name == user_input['user_name']
    assert user.email == user_input['email']

def test_comparison():
    user1 = User.from_dict(user_input)
    user2 = User.from_dict(user_input)

    assert user1 == user2
