# django-custom-logging

[![Release](https://github.com/sh-cho/django-custom-logging/actions/workflows/release.yml/badge.svg)](https://github.com/sh-cho/django-custom-logging/actions/workflows/release.yml)
[![PyPI version](https://badge.fury.io/py/django-custom-logging.svg)](https://badge.fury.io/py/django-custom-logging)
[![PyPI - License](https://img.shields.io/pypi/l/django-custom-logging)](https://github.com/sh-cho/django-custom-logging/blob/master/LICENSE)

Django middleware for custom logging

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

(TBD)

## Examples
(TBD)
