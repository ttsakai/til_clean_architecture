from app.repository.in_memory_repository import InMemoryRepository
from app.use_case.user_list import UserList

data = [
    {'user_id':'hoge','user_name':'hoge','email':'hoge@example.com'},
    {'user_id':'hoga','user_name':'hoga','email':'hoga@example.com'},
    {'user_id':'foge','user_name':'foge','email':'foge@example.com'},
]

repository = InMemoryRepository(data)
use_case = UserList(repository)
result = use_case.execute()

print ([user.to_dict() for user in result])
