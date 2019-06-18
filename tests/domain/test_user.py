import pytest
import uuid
import json
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


def test_serialize():
    user1 = User.from_dict(user_input)
    expected_output = f'{{"user_id": "{ user1.user_id }", "user_name": "hoge", "email": "hoge@example.com"}}'

    assert json.dumps(user1, cls=user1.Serializer) == expected_output