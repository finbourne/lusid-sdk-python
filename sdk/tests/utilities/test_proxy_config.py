import unittest

from lusid.utilities import ProxyConfig


class ProxyConfigTests(unittest.TestCase):

    def test_format_schemas_with_port(self):
        """
        Tests that the proxy can be formatted correctly with a port

        :return: None
        """
        proxy_config = ProxyConfig(
            address="http://localhost:8888",
            username="username",
            password="password"
        )

        formatted = proxy_config.format_proxy_schema()

        expected = {
            "http": "http://username:password@localhost:8888",
            "https": "http://username:password@localhost:8888"
        }

        self.assertEqual(expected, formatted)

    def test_format_schemas_no_port(self):
        """
        Tests that the proxy can be formatted correctly without a port

        :return: None
        """
        proxy_config = ProxyConfig(
            address="http://localhost",
            username="username",
            password="password"
        )

        formatted = proxy_config.format_proxy_schema()

        expected = {
            "http": "http://username:password@localhost",
            "https": "http://username:password@localhost"
        }

        self.assertEqual(expected, formatted)

    def test_create_proxy_no_protocol(self):
        """
        Tests that the proxy won't be created without a fully qualified address

        :return: None
        """

        with self.assertRaises(ValueError) as ex:
            ProxyConfig(
                address="localhost",
                username="username",
                password="password"
            )

        self.assertEqual(
            ex.exception.args[0],
            f"The provided proxy address of localhost does not contain a protocol, please specify in the full format e.g. http://myproxy.com:8080")
