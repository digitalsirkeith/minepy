from .context import minepy
from config import protocol
import pytest

class Test_Connection:
    """
    Test for the connection to the server
    """
    address = 'localhost'
    port = 25565

    @pytest.fixture(autouse=True, scope='class')
    def setup_connection(self):
        self.connection = minepy.network.connection.Connection(address=self.address, port=self.port)

    def test_handshake(self):
        assert self.connection.login()