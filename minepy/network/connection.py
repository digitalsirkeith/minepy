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
    
    def connect(self)
        try:
            self.socket.connect((self.address, self.port))
        except:
            logger.exception('Connection: Failed to connect')
        
    def start_handshake(self):
        login_packet = protocol.handshake.login()
        