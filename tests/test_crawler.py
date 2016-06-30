import pytest
from sitemapgenerator.crawler import Crawler


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
def test_run(path, links_all, links_unvisited, httpbin):
    c = Crawler(httpbin.url)
    c.run(url=path, recurse=False)

    assert c.links.keys() == links_all.keys()
    for k, v in c.links.items():
        assert 'soup' in v
        assert 'visited' not in v

    assert c.get_unvisited_links().sort() == links_unvisited.sort()


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
def test_run_recursion(path, links_all, links_unvisited, httpbin):
    c = Crawler(httpbin.url)
    c.run(url=path, recurse=True, throttle=0)

    assert c.links.keys() == links_all.keys()
    for k, v in c.links.items():
        assert 'soup' in v
        if c.get_unvisited_links():
            assert 'visited' in v

    assert c.get_unvisited_links().sort() == links_unvisited.sort()
