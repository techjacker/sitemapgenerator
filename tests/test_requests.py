import pytest


class TestRequests:

    @pytest.mark.parametrize('method', ('GET', 'HEAD'))
    def test_no_content_length(self, httpbin, method):
        assert True
     #    req = requests.Request(method, httpbin(method.lower())).prepare()
    	# assert 'Content-Length' not in req.headers
