import logging
from functools import reduce
from logging import Filter, LogRecord

from . import local_thread, PLACEHOLDER
from .exceptions import CaptureListValidationException
from .utils import getattrd


logger = logging.getLogger(__name__)


class CustomFilter(Filter):
    def __init__(self, capture_list=None, *args, **kwargs):
        super().__init__()
        if not isinstance(capture_list, (list, tuple)):
            raise CaptureListValidationException

        self.capture_list = capture_list or None

        # TODO: Check if this really right methodology
        # FIXME: multiple handlers?
        # NOTE: be careful with `map`
        format_str = logger.handlers[0].formatter._fmt
        capture_outs = map(lambda x: x[1], capture_list)
        capture_outs_format = reduce(
            lambda x, y: f"{x} {y}",
            map(lambda x: f"{{{x}}}", capture_outs)
        )
        logger.handlers[0].formatter._fmt = format_str.replace(PLACEHOLDER, capture_outs_format, 1)

        # TODO: args, kwargs

    def filter(self, record: LogRecord) -> bool:
        for capture_in, capture_out in self.capture_list:
            # FIXME: default value should be differ by its type
            setattr(record, capture_out, getattrd(local_thread, capture_in, "-"))

        return True
