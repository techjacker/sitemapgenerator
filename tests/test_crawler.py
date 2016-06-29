import pytest
# import pprint
from sitemapgenerator.crawler import Crawler


@pytest.mark.parametrize(('path', 'expected'), [
    ('/html', {}),
    ('/encoding/utf8', {
        'http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt': {
            'soup': {}
        }
    }),
    ('/links/1/1', {
        '/links/1/0': {
            'soup': {}
        }
    })
])
def test_extract_links(path, expected, httpbin):
    c = Crawler()
    res = c.run(httpbin + path)
    assert res.keys() == expected.keys()

    for k, v in res.items():
        assert 'soup' in v
        assert 'visited' not in v
