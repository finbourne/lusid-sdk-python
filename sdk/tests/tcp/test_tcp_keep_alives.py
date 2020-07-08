import unittest

from lusid.tcp.tcp_keep_alive_probes import TCPKeepAliveValidationMethods


class MockSocket:
    """
    Mocks an SSL socket that is missing an .ioctl or .setsockopts method.
    """
    def __init__(self):
        """
        No need to initialise anything here as it is an empty class which is missing
        a .ioctl and .setsockopts method
        """
        pass


class MockConnection:
    """
    Mocks a connection with an SSL socket
    """
    def __init__(self, sock):
        """
        :param sock: The socket to use with the connection
        """
        self.sock = sock


class TestTCPKeepAlives(unittest.TestCase):

    def test_wrapped_socket_no_attributes_does_not_throw(self):
        """
        Tests that if the provided socket is missing the function required to set the socket options,
        the socket options are left as is, rather than an AttributeError being raised

        :return: None
        """

        TCPKeepAliveValidationMethods.adjust_connection_socket(MockConnection(sock=MockSocket()))
