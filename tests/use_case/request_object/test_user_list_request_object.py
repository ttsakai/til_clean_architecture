import pytest
from app.use_case.request_object import user_list_request_object as req

accepted_filters = [{'name':'hoge'}]
rejected_filters = [{'email':'hugahuga'}]

class TestUserListRequestObject:
    def test_without_parameters(self):
        request = req.UserListRequestObject()

        assert request.filters is None
        assert bool(request) is True

    def test_from_emplty_dict(self):
        request = req.UserListRequestObject.from_dict({})

        assert request.filters is None
        assert bool(request) is True

    def test_empty_filters(self):
        request = req.UserListRequestObject(filters={})

        assert request.filters == {}
        assert bool(request) is True

    def test_from_dict_empty_filters(self):
        request = req.UserListRequestObject.from_dict({'filters':{}})

        assert request.filters == {}
        assert bool(request) is True


    def test_from_dict_with_wrong_filters(self):
        request = req.UserListRequestObject.from_dict({'filters':{'msg':'hugaaa'}})

        assert request.has_errors()
        assert request.errors[0]['parameter'] == 'filters'
        assert bool(request) is False


    def test_from_dict_with_invalid_filters(self):
        request = req.UserListRequestObject.from_dict({'filters':5})

        assert request.has_errors()
        assert request.errors[0]['parameter'] == 'filters'
        assert bool(request) is False

    @pytest.mark.parametrize('filters',accepted_filters)
    def test_from_dict_with_accepted_filters(self,filters):
        request = req.UserListRequestObject.from_dict({'filters':filters})

        assert request.filters == filters
        assert bool(request) is True

    @pytest.mark.parametrize('filters',rejected_filters)
    def test_from_dict_with_rejected_ilters(self,filters):
        request = req.UserListRequestObject.from_dict({'filters':filters})

        assert request.has_errors()
        assert request.errors[0]['parameter'] == 'filters'
        assert bool(request) is False
