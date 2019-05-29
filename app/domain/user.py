class User:

    def __init__(self, user_id, user_name, email):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email

    @classmethod
    def from_dict(cls,adict):
        return cls(**adict)

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
