import time

import mesop as me
import mesop.labs as mel

import threading

from absl import flags

from mesop.runtime import enable_debug_mode
from mesop.server.constants import EDITOR_PACKAGE_PATH, PROD_PACKAGE_PATH
from mesop.server.logging import log_startup
from mesop.server.server import configure_flask_app
from mesop.server.static_file_serving import configure_static_file_serving
from mesop.utils.host_util import get_default_host


@me.page(title="Home")
def home():
    me.text("Hello, world")


@me.page(path="/text_to_text", title="Text I/O Example")
def app():
    mel.text_to_text(
        upper_case_stream,
        title="Text I/O Example",
    )


def upper_case_stream(s: str):
    yield s.capitalize()
    time.sleep(0.5)
    yield "Done"



