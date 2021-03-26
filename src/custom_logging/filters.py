import logging

from . import local_thread
from .utils import getattrd


class UserIdFilter(logging.Filter):
    def filter(self, record):
        record.user_id = getattrd(local_thread, "request.user.id", -1)
        return True
