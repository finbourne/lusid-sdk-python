class ProxyConfig:
    """
    This class is used to hold the proxy configuration details
    """

    def __init__(self, address, username=None, password=None):
        """
        :param str address: The address of the proxy including the port e.g. https://myproxy.com:8080
        :param str username: The username for the proxy
        :param str password: The password for the proxy
        """
        self.address = address
        self.__username = username
        self.__password = password

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):

        if "http://" not in address and "https://" not in address:
            raise ValueError(f"The provided proxy address of {address} does not contain a protocol, please specify in the full format e.g. http://myproxy.com:8080")

        self.__address = address

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    def format_proxy_schema(self):
        """
        Takes the proxy details and converts them into a dictionary format to be used with other libraries e.g. requests

        :return: dict: A dictionary with the http and https proxy details including username and password
        """

        proxy_url = self.address

        # Only run if there is a username and password
        if self.username is not None and self.password is not None:
            index = self.address.index("://")

            proxy_url = f"{self.address[0:index + 3]}{self.username}:{self.password}@{self.address[index + 3:]}"

        return {
            "http": proxy_url,
            "https": proxy_url
        }
