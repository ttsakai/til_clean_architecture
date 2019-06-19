from app.use_case.request_object import user_list_request_object as req
from app.use_case.response_object import response_object as res

class TestResponseOject:
    def test_success(self):
        assert bool(res.ResponseSuccess()) is True
