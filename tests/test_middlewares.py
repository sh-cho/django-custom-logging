import unittest
from unittest.mock import Mock

from src.custom_logging import local_thread
from src.custom_logging.middlewares import capture_request


class TestMiddleware(unittest.TestCase):
    def setUp(self):
        # clear local_thread
        if getattr(local_thread, "request", None):
            del local_thread.request

    def test_capture_request(self):
        request = Mock()
        middleware = capture_request(Mock())

        self.assertIsNone(getattr(local_thread, "request", None))
        middleware(request)
        self.assertIsNotNone(getattr(local_thread, "request", None))


if __name__ == "__main__":
    unittest.main()
