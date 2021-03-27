# django-custom-logging

[![Release](https://github.com/sh-cho/django-custom-logging/actions/workflows/release.yml/badge.svg)](https://github.com/sh-cho/django-custom-logging/actions/workflows/release.yml)
[![PyPI version](https://badge.fury.io/py/django-custom-logging.svg)](https://badge.fury.io/py/django-custom-logging)
[![PyPI - License](https://img.shields.io/pypi/l/django-custom-logging)](https://github.com/sh-cho/django-custom-logging/blob/master/LICENSE)

Django middleware for custom logging

(Not ready to use yet!)


## Installation
1. Install the package
    ```sh
    python -m pip install django-custom-logging
    ```
1. Add middleware to `MIDDLEWARE` in setting file
    ```python
    MIDDLEWARE = (
        # other middlewares ...
        "django-custom-logging.middleware.request_info_middleware",
    )
    ```
1. Finally, add `custom_logging.filters.UserIdFilter` to `LOGGING` in setting file and update formatter
    ```python
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d [USER_ID:%(user_id)d] %(message)s",
            },
        },
        "filters": {
            "user_id_filter": {
                "()": "custom_logging.filters.UserIdFilter",
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
                "filters": ["user_id_filter"],
            },
        },
        "root": {"level": "INFO", "handlers": ["console"]},
    }
    ```


## How to log?
In order to log with 


## Example logs
```
INFO 2021-03-25 11:33:25,263 credentials 35052 4748750336 [USER_ID:-1] Found credentials in shared credentials file: ~/.aws/credentials
INFO 2021-03-25 11:33:25,505 views 35052 4748750336 [USER_ID:33] message1
INFO 2021-03-25 11:33:25,508 views 35052 4748750336 [USER_ID:33] message2
```
