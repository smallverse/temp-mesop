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


# ----------------------------------------------------------------

def run_mesop(host: str | None = None, port: int = 32123, prod_mode: bool = False):
    """
    When running in Colab environment, this will launch the web server.
    https://github.com/google/mesop/blob/273c65d26f710f19504525b7295e101430f284d5/mesop/colab/colab_run.py#L9
    Otherwise, this is a no-op.
    """

    # Ensures the flags are marked as parsed before creating the app otherwise you will
    # get UnparsedFlagAccessError.
    #
    # Depending on the Colab environment, the flags may or may not be parsed.
    #
    # Note: this ignore all Mesop CLI flags, but we could provide a way to override
    # Mesop defined flags in the future if necessary.
    if not flags.FLAGS.is_parsed():
        flags.FLAGS.mark_as_parsed()
    flask_app = configure_flask_app(prod_mode=prod_mode)
    if not prod_mode:
        enable_debug_mode()

    configure_static_file_serving(
        flask_app,
        static_file_runfiles_base=PROD_PACKAGE_PATH
        if prod_mode
        else EDITOR_PACKAGE_PATH,
    )

    log_startup(port=port)

    if host is None:
        host = get_default_host()

    def run_flask_app():
        flask_app.run(host=host, port=port, use_reloader=False)

    # Launch Flask in background thread so we don't hog up the main thread
    # for regular Colab usage.
    threading.Thread(target=run_flask_app).start()


def run():
    run_mesop(host="0.0.0.0", port=8080, prod_mode=False)


if __name__ == '__main__':
    run()
