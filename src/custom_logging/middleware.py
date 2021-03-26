import logging

from . import local_thread

logger = logging.getLogger(__name__)


def request_info_middleware(get_response):
    def middleware(request):
        local_thread.request = request or None
        return get_response(request)
    return middleware
