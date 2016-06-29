#!/usr/bin/env python3
import argparse
from sitemapgenerator.crawler import Crawler


def main():
    parser = argparse.ArgumentParser(
        description='Generate an XML sitemap for a domain'
    )
    parser.add_argument('domain', type=str, help='domain to crawl')
    parser.add_argument('-f', '--file', help='write the xml to a file')
    parser.add_argument('-t', '--throttle', help='max time in secs to wait between requesting URLs')
    parser.add_argument('-q', '--quiet', action='store_true')
    args = parser.parse_args()

    crawler = Crawler(args.domain, args.quiet, args.throttle)
    crawler.run(recurse=True)

if __name__ == '__main__':
    main()
