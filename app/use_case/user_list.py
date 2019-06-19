from app.use_case.response_object import response_object as res

class UserList:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, request):
        users = self.repository.list()
        return res.ResponseSuccess(users)