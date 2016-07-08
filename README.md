# sitemapgenerator

Creates an XML sitemap of a domain.

Python3+.

## Install
```
pip install sitemapgenerator
```


## Usage

```Shell
usage: sitemapgenerator [-h] [-f FILE] [-t THROTTLE] [-l LIMIT] [-q] domain

Generate an XML sitemap for a domain

positional arguments:
  domain                domain to crawl

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  write the xml to a file
  -t THROTTLE, --throttle THROTTLE
                        max time in secs to wait between requesting URLs
  -l LIMIT, --limit LIMIT
                        max number of URLs to crawl
  -q, --quiet
```



## Example Usage
```Shell
$ sitemapgenerator -f site.xml -l 1 devopsreactions.tumblr.com

crawling homepage
crawling /post/146054449345/ops-report-three-out-of-five-app-servers#notes
crawled 2 URLs
wrote sitemap to /tmp/site.xml
```


-----------------------------------------------------------

## Development

### Setup

#### Set up virtualenv
```
pyenv install 3.5.0
pyenv local 3.5.0
pyvenv env
source env/bin/activate
```

#### Install requirements
```
pip install -r requirements.txt
```

#### Update requirements
```
pip install -r requirements-to-freeze.txt --upgrade
pip freeze > requirements.txt
```

-----------------------------------------------------------

## Tests

```
py.test tests -q
```


-----------------------------------------------------------

## TODO

- add more tests
- normalize URLs to remove dupes
	- hashes from end of URLs (eg /some/url/#respond)
	- tailing slashes on URLs
- add option to create sitemap of:
  - external URLs
  - non HTML URLs on same domain
- refactor code
  - create separate data class which crawler inherits from/accesses
  - create single getter method for ```Crawler``` class links and remove extra get_* methods
- add concurrency (eventlet/gevent)
- add progress bar to CLI
- add support for Python 2
  - add tox tests for different python versions

