# comp-emp
Project developed for technical challenge

![Django CI](https://github.com/vitorpvcampos/comp-emp/workflows/Django%20CI/badge.svg)
[![Updates](https://pyup.io/repos/github/vitorpvcampos/comp-emp/shield.svg)](https://pyup.io/repos/github/vitorpvcampos/comp-emp/)
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django 3.1.3](https://img.shields.io/badge/django-3.1.3-blue.svg)](https://www.djangoproject.com/download/)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/vitorpvcampos/django-e-learning/blob/main/LICENSE)
[![codecov](https://codecov.io/gh/vitorpvcampos/comp-emp/branch/main/graph/badge.svg?token=0BDA2I3QRK)](https://codecov.io/gh/vitorpvcampos/comp-emp)

This project was developed as a requirement of a selective process for a vacancy as a Backend Developer. 

The objective was to implement an application with  system to manage companies and its employees, using any Python web framework (in this case, I used [Django](https://docs.djangoproject.com/en/3.1/)) and a [GraphQL](https://graphql.org/learn/) API.

As differentials:
* CPF and CNPJ validation for employees and companies
* Tests
* Containerized Docker application

## How to run the project?

### Cloning the repository and creating the ```.env``` file
Supposing you have ```git``` and ```python``` >= ```3.9.0``` installed (not tested on older versions):

```
git clone https://github.com/vitorpvcampos/comp-emp.git
cd comp-emp
cp contrib/env-sample .env
pip install --upgrade pip
pip install pipenv
pipenv install --dev
```

### Using Docker with Docker Compose and running the migrations:

```
docker-compose build
docker-compose up -d
docker-compose run app python manage.py migrate
docker-compose run app python manage.py createsuperuser
```

#### PEP8 lint
```
pipenv run flake8
```

#### Testing with pytest
```
pipenv run pytest --cov=compemp
```

##### Work environment

The project was developed using an iMac Pro (via ```OpenCore 0.6.3```) running macOS Big Sur version 11.0.1 and the IDE PyCharm Professional 2020.2.3. The implementation was also tested on an AMD machine running the Linux distribution POP!_OS 20.10, with the same IDE.