"""
Connection Class
"""

import socket
from minepy.logger import logger
from config import protocol

class Connection:
    def __init__(self, address, port=25565, auth_token=None, username=None):
        self.socket                 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address                = address
        self.port                   = port
        self.auth_token             = auth_token
        self.username               = username
        self.compression_enabled    = False
    
    def connect(self):
        try:
            self.socket.connect((self.address, self.port))
        except:
            logger.exception('Connection: Failed to connect')
            return

        try: 
            self.start_login()
        except:
            return
        
    def start_login(self):
        login_packet = protocol.packet.serverbound.handshake.login.with_host(addr=self.address, port=self.port)
        self.send_packet(login_packet)
        
    def send_packet(self, packet: protocol.packet.Packet):
        """
        TODO: Encode the packet and send over the socket
        """
        data = packet.encode(compression_enabled=self.compression_enabled)
        self.socket.send(data)
        pass