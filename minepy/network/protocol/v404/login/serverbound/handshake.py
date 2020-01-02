"""
Handshake packets
"""

from minepy.datatypes.minecraft import VarInt, ByteArray
from ... import Packet
from ... import version

class HandshakePacket(Packet):
    """
    Handshake Packet
    A clientbound packet for initiating connections
    """
    def __init__(self, next_state: int):
        super().__init__(id=VarInt(0x00), data=ByteArray(None))
        self.protocol_version   = version
        self.addr               = ''
        self.port               = 0
        self.next_state         = next_state

    def encode_to_data(self):
        """
        TODO: encode protocol, addr, port, and next_state into data
        """
        pass

    def with_host(self, addr: str='', port: int=0, next_state: int=0):
        """
        TODO: set values for addr, port
        """
        self.encode_to_data()
        
        return self

login = HandshakePacket(1)
status = HandshakePacket(2)