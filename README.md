# django-custom-logging

[comment]: <> ([![Release]&#40;https://github.com/sh-cho/django-custom-logging/actions/workflows/release.yml/badge.svg&#41;]&#40;https://github.com/sh-cho/django-custom-logging/actions/workflows/release.yml&#41;)
[![Test](https://github.com/sh-cho/django-custom-logging/actions/workflows/test.yml/badge.svg)](https://github.com/sh-cho/django-custom-logging/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/django-custom-logging)](https://pypi.python.org/pypi/django-custom-logging/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-custom-logging)](https://pypi.python.org/pypi/django-custom-logging/)
[![PyPI - License](https://img.shields.io/pypi/l/django-custom-logging)](https://github.com/sh-cho/django-custom-logging/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Django middleware for custom format logging


## Installation
1. Install the package
```sh
python -m pip install django-custom-logging
```
2. Add adequate middlewares to `MIDDLEWARE` in setting file. Current version only supports a middleware that captures `request` into local thread(`threading.local()`)
```python
MIDDLEWARE = (
    # other middlewares ...
    "custom_logging.middlewares.capture_request",
)
```
3. Add `custom_logging.filters.CustomFilter` to `LOGGING` in setting file and set `capture_list` containing a list of variables to be captured(`capture_in`) and format string to be printed(`capture_out`). Also add filter on handler's filter list.
```python
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d}"
                      " [USER_ID:{user_id}] {message}",
                                #^^^^^^^^^ - (A)
            "style": "{",
        },
    },
    "filters": {
        "custom_filter": {
        #^^^^^^^^^^^^^ - (B)
            "()": "custom_logging.filters.CustomFilter",
            "capture_list": (
                # (capture_in, capture_out)
                ("request.user.id", "user_id"),
                                    #^^^^^^^ - (A)
            ),
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "filters": ["custom_filter"],
                        #^^^^^^^^^^^^^ - (B)
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}
```
Note that you can use any format styles(%, {, $), but should make format arguments with `str` type. For example, if you want to capture `request.user.id` as `user_id`, please follow format below.
```
%-style: %(user_id)s
{-style: {user_id}
$-style: ${user_id}
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
INFO 2021-03-25 11:33:25,170 credentials 35052 4748750336 [USER_ID:-] Found credentials in shared credentials file: ~/.aws/credentials
INFO 2021-03-25 11:33:25,505 views 35052 4748750336 [USER_ID:33] example log
```


## Supported versions
- Python: >=3.6
- Django: >=3
