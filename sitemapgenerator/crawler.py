import re
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from numbers import Number


class Crawler:

    def __init__(self, domain, quiet=False, throttle_max=3):
        self.set_domain(domain)
        self.quiet = quiet
        self.throttle_max = throttle_max
        self.links = {}
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0'}

    def set_domain(self, domain):
        if not domain:
            raise Exception('domain must be defined')

        if not domain.startswith('http://') and \
                not domain.startswith('https://'):
            domain = 'http://' + domain

        self.domain = domain

    def extract_links(self, contents):
        soup = BeautifulSoup(contents, 'html.parser')
        return {
            a.get('href'): {"soup": a}
            for a in soup.find_all('a')
            if a.get('href') is not None and not a.get('href').startswith('#')
        }

    def request_url(self, url):
        res = requests.get(url, headers=self.headers).text
        # set visited flag
        if self.strip_domain(url) in self.links:
            self.links[self.strip_domain(url)]['visited'] = True
        return res

    def strip_domain(self, url):
        return re.sub('^' + re.escape(self.domain), '', url)

    def merge_links(self, links, url):
        for k, v in links.items():

            # strip domain on internal links
            if k.strip().startswith(self.domain):
                k = self.strip_domain(k)

            # add extra links if not homepage and not already in dict
            if k and k != '/' and k not in self.links:
                self.links[k] = v

    def get_domain_links(self):
        return {
            k: v for k, v in self.links.items() if not k.startswith('http')
        }

    def get_unvisited_links(self):
        return [
            k for k, v in self.get_domain_links().items() if 'visited' not in v
        ]

    def crawl(self, url=''):
        text = self.request_url(self.domain + url)
        links = self.extract_links(text)
        self.merge_links(links, url)

    def run(self, url='', recurse=False, throttle=None):

        if self.quiet is not True:
            # crawl homepage to start with
            print('crawling {}'.format(url if url else 'homepage'))

        self.crawl(url)

        if recurse is True:
            links_unvisited = self.get_unvisited_links()
            if links_unvisited:
                sleep(throttle if isinstance(throttle, Number)
                      else randint(0, self.throttle_max))
                return self.run(links_unvisited[0], recurse, throttle)

        return self.links
