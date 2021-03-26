import unittest

from mock import Mock

from . import local_thread
from custom_logging.middleware import request_info_middleware


class TestMiddleware(unittest.TestCase):
    def test_request(self):
        # clear local_thread
        if getattr(local_thread, "request", None):
            del local_thread.request

        request = Mock()
        middleware = request_info_middleware(Mock())

        self.assertIsNone(getattr(local_thread, "request", None))
        middleware(request)
        self.assertIsNotNone(getattr(local_thread, "request", None))


if __name__ == "__main__":
    unittest.main()
