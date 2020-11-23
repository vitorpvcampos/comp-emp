# comp-emp
Project developed for technical challenge

![Django CI](https://github.com/vitorpvcampos/comp-emp/workflows/Django%20CI/badge.svg)
[![Updates](https://pyup.io/repos/github/vitorpvcampos/comp-emp/shield.svg)](https://pyup.io/repos/github/vitorpvcampos/comp-emp/)
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django 3.1.3](https://img.shields.io/badge/django-3.1.3-blue.svg)](https://www.djangoproject.com/download/)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/vitorpvcampos/django-e-learning/blob/main/LICENSE)

### How to run the project?

* Clone the repository
* Create a virtual environment with pipenv
* Set .env
* Install the dependencies
* Run docker-compose.yml
* Run the migrations

```
git clone https://github.com/vitorpvcampos/comp-emp.git
cd comp-emp
cp contrib/env-sample .env
pip install --upgrade pip
pip install pipenv
pipenv install --dev
docker-compose.yml up -d
python manage.py migrate
```

#### PEP8 lint
```
pipenv run flake8
```