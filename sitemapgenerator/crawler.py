import re
import requests
from bs4 import BeautifulSoup
from time import sleep


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

    def extract_links(self, contents):
        soup = BeautifulSoup(contents, 'html.parser')
        return {a.get('href'): {"soup": a} for a in soup.find_all('a')}

    def request_url(self, url):
        res = requests.get(url).text
        # set visited flag
        if self.strip_domain(url) in self.links:
            self.links[self.strip_domain(url)]['visited'] = True
        return res

    def strip_domain(self, url):
        return re.sub('^' + re.escape(self.domain), '', url)

    def merge_links(self, links, url):
        for k, v in links.items():
            # strip domain on internal links
            if k.startswith(self.domain):
                k = self.strip_domain(k)
            # add extra links if not homepage and not already in dict
            if k and k != '/' and k not in self.links:
                self.links[k] = v

    def get_domain_links(self):
        return {k: v for k, v in self.links.items() if not k.startswith('http')}

    def get_unvisited_links(self):
        return [k for k, v in self.get_domain_links().items() if 'visited' not in v]

    def crawl(self, url=''):
        text = self.request_url(self.domain + url)
        links = self.extract_links(text)
        self.merge_links(links, url)

    def run(self, url='', recurse=False, throttle=1):
        # crawl homepage to start with
        self.crawl(url)

        if recurse is True:
            links_unvisited = self.get_unvisited_links()
            if links_unvisited:
                sleep(throttle)
                return self.run(links_unvisited[0], recurse, throttle)

        return self.links
