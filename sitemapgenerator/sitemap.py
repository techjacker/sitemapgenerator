import os
from xml.etree.ElementTree import Element, SubElement, tostring
import pprint


class Sitemap:

    def __init__(self, filename, quiet=False):
        self.validate(filename)
        self.filepath = os.path.join(os.getcwd(), filename)
        self.quiet = quiet

    def validate(self, filename):
        if not filename:
            raise Exception('need to specify filename to write to')

    def write_to_file(self, contents):
        with open(self.filepath, 'w') as sitemap:
            sitemap.write()

    def run(self, links):
        if self.quiet is not True:
            print('wrote sitemap to {}'.format(self.filepath))
