"""
Packet Base Class
"""

from minepy.datatypes import minecraft

class Packet:
    """
    Packet Class
    Basic unit of communication for the minecraft protocol.
    """
    def __init__(self, id: minecraft.VarInt, data: minecraft.ByteArray):
        self.length = id.length + data.length
        self.id     = id
        self.data   = data

    def encode(self, compression_enabled: bool=False) -> bytes:
        """
        TODO. Transforms the class into a byte stream ready for transmission. Encoding depends on compression
        """
        return None
    
    @classmethod
    def decode(cls, raw_data):
        """
        TODO. Creates a Packet Object from raw_data
        """
        packet_id       = None
        packet_data     = None

        return Packet(packet_id, packet_data)

        
        