from . import local_thread


def capture_request(get_response):
    def middleware(request):
        local_thread.request = request or None
        return get_response(request)
    return middleware
