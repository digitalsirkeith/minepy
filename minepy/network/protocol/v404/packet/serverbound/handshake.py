"""
Handshake packets
"""

from minepy.datatypes.minecraft import VarInt, ByteArray
from ...packet import Packet
from ... import version
import config

class HandshakePacket(Packet):
    """
    Handshake Packet
    A clientbound packet for initiating connections
    """
    def __init__(self):
        super().__init__(id=VarInt(0x00), data=ByteArray(None))
        self.protocol_version   = version
        self.addr               = ''
        self.port               = 0
        self.next_state         = 0

    def encode_to_data(self):
        """
        TODO: encode protocol, addr, port, and next_state into data
        """
        pass

    def set_values(self, addr: str='', port: int=0, next_state: int=0):
        """
        TODO: set values for addr, port, and next_state
        """
        self.encode_to_data()