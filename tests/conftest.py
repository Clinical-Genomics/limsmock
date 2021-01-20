import pytest

from limsmock.server import run_server

import threading
import time


@pytest.fixture
def server_test1():
    file_path = "tests/fixtures/test_1"

    thread = threading.Thread(target=run_server, args=(file_path,))
    thread.daemon = True
    thread.start()
    time.sleep(0.1)
