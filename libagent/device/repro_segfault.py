"""Following https://github.com/romanz/trezor-agent/issues/157."""
import time

from . import interface, trezor
from .. import util

util.setup_logging(util.logging.DEBUG)

t = trezor.Trezor()
i = interface.Identity(identity_str='ssh://foo@bar.com', curve_name='nist256p1')

while True:
    with t:
        sig = t.sign(i, b'BLOB')
    time.sleep(60*10)
