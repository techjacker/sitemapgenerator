import pytest
from sitemapgenerator.crawler import Crawler


@pytest.fixture(params=[(True, 0), (False, 10000)])
def recurse(request):
    return request.param


@pytest.mark.parametrize(('path', 'links_all', 'links_unvisited'), [
    ('/html', {}, []),
    ('/encoding/utf8', {
        'http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt': {
            'soup': {}
        }
    }, []),
    ('/links/1/1', {
        '/links/1/0': {
            'soup': {}
        }
    }, ['/links/1/0']),
    ('/links/2/2', {
        '/links/2/1': {
            'soup': {}
        },
        '/links/2/0': {
            'soup': {}
        }
    }, ['/links/2/1', '/links/2/0'])
])
def test_run(path, links_all, links_unvisited, httpbin, recurse):
    c = Crawler(httpbin.url)
    c.run(url=path, recurse=recurse[0], throttle=recurse[1])

    assert c.links.keys() == links_all.keys()
    for k, v in c.links.items():
        assert 'soup' in v
        if recurse[0] is False:
            assert 'visited' not in v
        else:
            if k.startswith('http'):
                assert 'visited' not in v
            else:
                assert 'visited' in v

    if recurse[0] is False:
        assert sorted(list(c.unvisited_links)) == sorted(links_unvisited)
    else:
        assert list(c.unvisited_links) == []
