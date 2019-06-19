import collections
from app.use_case.request_object.invalid_request_object import InvalidRequestObject

class UserListRequestObject:
    accepted_filters = ['name']

    def __init__(self, filters=None):
        self.filters = filters


    @classmethod
    def from_dict(cls, adict):
        if 'filters' in adict.keys():
            invalid_req = InvalidRequestObject()
            if not isinstance(adict['filters'], collections.Mapping):
                invalid_req.add_error('filters', 'Is Not Iterable')
                return invalid_req

            for key, value in adict['filters'].items():
                if key not in cls.accepted_filters:
                    invalid_req.add_error('filters', f"{key} can not be used")

            if invalid_req.has_errors():
                return invalid_req

        return cls(filters=adict.get('filters',None))

    def __bool__(self):
        return True


