
### Development Setup




-----------------------------------------------------------

### Development Setup

#### Set up virtual environment & python version
```Shell
pyenv virtualenv 3.5.0 sitemapgenerator
pyenv local sitemapgenerator
pyvenv env
source env/bin/activate
```
Subsequently just ```source env/bin/activate```.

#### Install requirements
```
pip install -r requirements.txt
```

#### Update requirements
```
pip install -r requirements-to-freeze.txt --upgrade
pip freeze > requirements.txt
```
