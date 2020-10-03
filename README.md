# Space Age contact API

# Pre-requisites
You need `pipenv` to install all the required dependencies.

To install it just use:
```shell
$ pip install pipenv
```

# Installation
To install all dependencies, use the following command:
```shell
$ pipenv install
```


# Execution
To start the backend administrator, execute the following:
```shell
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

# Testing
Go to `http://127.0.0.1:8000` and login using the credentials created in the last step.

