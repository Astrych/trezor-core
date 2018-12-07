from trezor import wire
from trezor.messages import MessageType

from apps.common import HARDENED


def boot():
    ns = [["secp256k1", HARDENED | 44, HARDENED | 144]]
    wire.add(MessageType.RippleGetAddress, __name__, "get_address", ns)
    wire.add(MessageType.RippleSignTx, __name__, "sign_tx", ns)
