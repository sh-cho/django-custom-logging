# django-custom-logging
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
