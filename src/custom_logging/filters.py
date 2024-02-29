import logging
from logging import Filter, LogRecord

from . import local_thread
from .exceptions import CaptureListValidationException
from .utils import getattrd

logger = logging.getLogger(__name__)


class CustomFilter(Filter):
    def __init__(self, capture_list=None, default_values=None, *args, **kwargs):
        super().__init__()
        if not isinstance(capture_list, (list, tuple)):
            raise CaptureListValidationException

        self.capture_list = capture_list
        self.default_values = default_values or {}

    def filter(self, record: LogRecord) -> bool:
        for capture_in, capture_out in self.capture_list:
            # FIXME: default value should be differ by its type
            setattr(
                record, capture_out, getattrd(local_thread, capture_in, None) or self.default_values.get(capture_out, None)
            )

        return True
