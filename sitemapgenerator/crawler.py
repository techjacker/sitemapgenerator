import re
import pprint
import requests
from bs4 import BeautifulSoup


class Crawler:

    def __init__(self, domain):
        self.set_domain(domain)
        self.links = {}

    def set_domain(self, domain):
        if not domain:
            raise Exception('domain must be defined')

        if not domain.startswith('http://') and \
                not domain.startswith('https://'):
            self.domain = 'http://' + domain

        self.domain = domain
        print('')
        print('self.domain')
        pprint.pprint(self.domain)
        print('')

    def extract_links(self, contents):
        soup = BeautifulSoup(contents, 'html.parser')
        return {a.get('href'): {"soup": a} for a in soup.find_all('a')}

    def request_url(self, url):
        return requests.get(url).text

    def merge_links(self, links):
        for k, v in links.items():
            # strip domain on internal links
            if k.startswith(self.domain):
                k = re.sub('^' + re.escape(self.domain), '', k)
            if k not in self.links:
                self.links[k] = v

    def get_domain_links(self):
        return {k: v for k, v in self.links.items() if not k.startswith('http')}

    def get_unvisited_links(self):
        return [k for k, v in self.get_domain_links().items() if 'visited' not in v]

    def run(self, url='', recurse=False):
        text = self.request_url(self.domain + url)
        links = self.extract_links(text)
        self.merge_links(links)

        if recurse is True:
            links_unvisited = self.get_unvisited_links()
            if links_unvisited:
                return self.run(links_unvisited[0], recurse)

        return self.links
