import requests
from bs4 import BeautifulSoup


class Crawler:

    def __init__(self):
        print("inited")
        self.links = []

    def extract_links(self, contents):
        soup = BeautifulSoup(contents, 'html.parser')
        return [a.get('href') for a in soup.find_all('a')]

    def request_url(self, url):
        return requests.get(url).text

    def run(self, url):
        text = self.request_url(url)
        links = self.extract_links(text)
        self.links += links
        return self.links
