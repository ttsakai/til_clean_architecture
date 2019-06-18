import json

class User:

    def __init__(self, user_id, user_name, email):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email

    @classmethod
    def from_dict(cls,adict):
        return cls(
            user_id=adict['user_id'],
            user_name=adict['user_name'],
            email=adict['email'],
        )

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_name':self.user_name,
            'email' : self.email,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    class Serializer(json.JSONEncoder):
        def default(self, o):
            try:
                to_serialize = {
                    'user_id':str(o.user_id),
                    'user_name':o.user_name,
                    'email':o.email,
                }
                return to_serialize
            except AttributeError:
                return super().default(o)