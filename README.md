# sitemapgenerator

Python3+.

## Install
```
pip install sitemapgenerator
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

- add concurrency (eventlet/gevent)
