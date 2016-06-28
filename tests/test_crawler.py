import pytest
# import pprint
from sitemapgenerator import crawler


@pytest.mark.parametrize(('path', 'expected'), [
    ('/html', []),
    # contains only an external link
    ('/encoding/utf8', []),
    ('/links/1/1', ['/links/1/0'])
])
def test_extract_links(path, expected, httpbin):
    c = crawler.Crawler()
    assert c.run(httpbin + path) == expected
