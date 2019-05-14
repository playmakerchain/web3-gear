import time
import click
import random
import requests
from .utils.thread import spawn
from .powerplay.client import powerplay
from .powerplay.account import (
    solo,
    keystore as _keystore,
)
from .rpc import (
    application,
    web3_clientVersion,
)
from wsgiref.simple_server import (
    make_server,
    WSGIRequestHandler,
)


class SilentWSGIRequestHandler(WSGIRequestHandler):
    """
    WSGIRequestHandler 会输出所有的 request info, 重写 log_request 以保持输出干净.
    """

    def log_request(self, code="-", size="-"):
        return


@click.command()
@click.option(
    "--host",
    default="127.0.0.1",
)
@click.option(
    "--port",
    default=4657,
    type=int,
)
@click.option(
    "--endpoint",
    default="http://127.0.0.1:4658",
)
@click.option(
    "--keystore",
    default="",
)
@click.option(
    "--passcode",
    default="",
)
def run_server(host, port, endpoint, keystore, passcode):
    try:
        response = requests.options(endpoint)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Unable to connect to PowerPlay-Restful server.")
        return

    print(web3_clientVersion())
    print("Listening on %s:%s" % (host, port))

    powerplay.set_endpoint(endpoint)
    if keystore == "":
        .set_accounts(solo())
    else:
        .set_accounts(_keystore(keystore, passcode))

    server = make_server(
        host,
        port,
        application,
        handler_class=SilentWSGIRequestHandler
    )
    spawn(server.serve_forever)

    try:
        while True:
            time.sleep(random.random())
    except KeyboardInterrupt:
        try:
            server.stop()
        except AttributeError:
            server.shutdown()


if __name__ == '__main__':
    run_server()
