```
       __  _                                
  ____/ / (_)___ _____  ____ _____          
 / __  / / / __ `/ __ \/ __ `/ __ \         
/ /_/ / / / /_/ / / / / /_/ / /_/ /         
\__,_/_/ /\__,_/_/ /_/\__, /\____/          
    /___/            /____/                 
      _______  _______/ /_____  ____ ___    
     / ___/ / / / ___/ __/ __ \/ __ `__ \   
    / /__/ /_/ (__  ) /_/ /_/ / / / / / /   
    \___/\__,_/____/\__/\____/_/ /_/ /_/    
           __                  _            
          / /___  ____ _____ _(_)___  ____ _
         / / __ \/ __ `/ __ `/ / __ \/ __ `/
        / / /_/ / /_/ / /_/ / / / / / /_/ / 
       /_/\____/\__, /\__, /_/_/ /_/\__, /  
               /____//____/        /____/   
```

[![PyPI](https://img.shields.io/pypi/v/django-custom-logging)](https://pypi.python.org/pypi/django-custom-logging/)
[![PyPI - License](https://img.shields.io/pypi/l/django-custom-logging)](https://github.com/sh-cho/django-custom-logging/blob/master/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-custom-logging)](https://pypi.python.org/pypi/django-custom-logging/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/django-custom-logging)](https://pypi.python.org/pypi/django-custom-logging/)
[![Test](https://github.com/sh-cho/django-custom-logging/actions/workflows/test.yml/badge.svg?branch=develop)](https://github.com/sh-cho/django-custom-logging/actions/workflows/test.yml)
[![Lint](https://github.com/sh-cho/django-custom-logging/actions/workflows/lint.yml/badge.svg?branch=develop)](https://github.com/sh-cho/django-custom-logging/actions/workflows/lint.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

django middleware for custom format logging


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
            "format": "{levelname} {asctime} {module} {meta[REMOTE_ADDR]} {meta[CONTENT_LENGTH]} {process:d} {thread:d}"
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
                ("request.META", "meta"),
            ),
            "default_values" : {
                "meta": {
                    "REMOTE_ADDR": "127.0.0.1",
                    "CONTENT_LENGTH": 0,
                }
            },
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

### ⚠️ Specifying Default Values
Default values should be provided if `capture_out` is object and its attribute can be undefined. (ex. `{meta[REMOTE_ADDR]}`)

For example, accessing request variable in filter while using scheduling cronjob(ex. `@shared_task`) can raise error because it is not HTTP request so `request` is not defined.

If `capture_out` is single value(ex. str, int, etc.), default value is not needed. It will be replaced with placeholder `-` if it is not defined.


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
INFO 2024-03-01 11:33:25,170 credentials 127.0.0.1 0 35052 4748750336 [USER_ID:-] Found credentials in shared credentials file: ~/.aws/credentials
INFO 2024-03-01 11:33:25,505 views 123.123.123.123 1000 35052 4748750336 [USER_ID:33] example log
```


## Supported versions
- Python: >=3.5
- Django: >=3

## License
See [LICENSE](./LICENSE)


## Contribution
Feel free to open issue or pull request.

### Contributors

<a href="https://github.com/sh-cho/django-custom-logging/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sh-cho/django-custom-logging" />
</a>
