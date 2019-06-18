from app.domain.user import User

class InMemoryRepository:
    
    def __init__(self, data):
        self.data = data 

    def list(self):
        return [User.from_dict(user) for user in self.data]
