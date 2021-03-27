# django-custom-logging

[![Release](https://github.com/sh-cho/django-custom-logging/actions/workflows/release.yml/badge.svg)](https://github.com/sh-cho/django-custom-logging/actions/workflows/release.yml)
[![PyPI version](https://badge.fury.io/py/django-custom-logging.svg)](https://pypi.python.org/pypi/django-custom-logging/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-custom-logging)](https://pypi.python.org/pypi/django-custom-logging/)
[![PyPI - License](https://img.shields.io/pypi/l/django-custom-logging)](https://github.com/sh-cho/django-custom-logging/blob/master/LICENSE)

Django middleware for custom format logging

⚠️ Currently pre-release version is only supported.


## Installation
1. Install the package
```sh
python -m pip install django-custom-logging
```
2. Add middleware to `MIDDLEWARE` in setting file
```python
MIDDLEWARE = (
    # other middlewares ...
    "django-custom-logging.middleware.request_info_middleware",
)
```
3. Add `custom_logging.filters.UserIdFilter` to `LOGGING` in setting file and update formatter, and add filter on handler's filter
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


## How to use
You can use `logger` just like before. No extra parameter is needed.

```python
import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class ExampleView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        logger.info("example log")
        return Response({"hello": "world!"}, status=status.HTTP_200_OK)
```

```
INFO 2021-03-25 11:33:25,505 views 35052 4748750336 [USER_ID:33] example log
```

## Supported versions
- Python: >=3.6
- Django: >=3
