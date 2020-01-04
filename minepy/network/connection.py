"""
Connection Class
"""

import socket
from minepy.logger import logger
from config import protocol

class Connection:
    def __init__(self, address: str, port: int=25565, auth_token=None, username: str=None):
        self.socket                 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address                = address
        self.port                   = port
        self.auth_token             = auth_token
        self.username               = username
        self.compression_enabled    = False
    
    def connect(self):
        """
        Set up TCP connection
        """
        try:
            self.socket.connect((self.address, self.port))
        except:
            logger.exception('Connection: Failed to connect')
            return False
        return True
        
    def login(self):
        """
        TODO: Perform the handshake with the server
        """
        try:
            data = protocol.data.packet['login']

            handshake_packet = protocol.login.serverbound.handshake.HandshakePacket(address=self.address, port=self.port)
            self.send_packet(handshake_packet)

            received_packet = self.receive_packet()
            if received_packet.id == data['success']['id']:
                # Connection is unencrypted and unauthenticated. Server operates in offline mode
                logger.info("Server is in offline mode.")
            else:
                # TODO: Finish encryption and compression process
                pass

        except:
            logger.exception('Connection: Failed to connect')
            return False

        return True
        
    def send_packet(self, packet: protocol.Packet):
        """
        TODO: Encode the packet and send over the socket
        """
        data = packet.encode(compression_enabled=self.compression_enabled)
        self.socket.send(data)
        pass

    def receive_packet(self) -> protocol.Packet:
        """
        TODO: waits for a packet from the server
        Planned: Add timeout when no keepAlive packet arrives within 30 seconds
        """
        return 0