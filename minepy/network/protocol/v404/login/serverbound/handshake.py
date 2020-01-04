"""
Handshake packets
"""

from minepy.datatypes.minecraft import VarInt, ByteArray
from ... import Packet
from ... import version
from ... import data

class HandshakePacket(Packet):
    """
    Handshake Packet
    A clientbound packet for initiating connections
    """
    def __init__(self, address: str='', port: int=25565, next_state: int=data.packet['login']['handshake']['id']):
        super().__init__(id=VarInt(data.packet['login']['handshake']['id']), data=ByteArray(None))
        self.protocol_version   = version
        self.address            = address
        self.port               = port
        self.next_state         = next_state

    def encode_to_data(self):
        """
        TODO: encode protocol, addr, port, and next_state into data
        """
        pass

class StatusPacket(HandshakePacket):
    """
    Status Packet
    """

    def __init__(self, address: str='', port: int=25565):
        super().__init__(address=address, port=port, next_state=data.state['status'])