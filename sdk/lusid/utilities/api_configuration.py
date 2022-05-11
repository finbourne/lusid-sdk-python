import re


class ApiConfiguration:

    def __init__(self, token_url=None, api_url=None, username=None, password=None, client_id=None, client_secret=None,
                 app_name=None, certificate_filename=None, proxy_config=None, access_token=None):
        """
        The configuration required to access LUSID, read more at https://support.finbourne.com/getting-started-with-apis-sdks

        :param str token_url: The token URL of the identity provider
        :param str api_url: The API URL for the LUSID client
        :param str username: The username to use
        :param str password: The password to use
        :param str client_id: The client id to use
        :param str client_secret: The client secret to use
        :param str app_name: The name of the application calling LUSID
        :param str certificate_filename: Name of the certificate file (.pem, .cer or .crt)
        :param lusid.utilities.ProxyConfig proxy_config: The proxy configuration to use
        """
        self.token_url = token_url
        self.__api_url = api_url
        self.__username = username
        self.__password = password
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__app_name = app_name
        self.__certificate_filename = certificate_filename
        self.__proxy_config = proxy_config
        self.__access_token = access_token

    @property
    def token_url(self):
        return self.__token_url

    @token_url.setter
    def token_url(self, value):
        def format_token_url(url: str) -> str:
            """
            Given an Okta issuer url (ie: https://lusid-testdomain.okta.com/oauth2/asd8f7a98sdf89a7ad), this function
            will return a full token url (ie: https://lusid-testdomain.okta.com/oauth2/asd8f7a98sdf89a7ad/v1/token)
            :param url: The url to format
            :return: An Okta token url (if the input is an Okta issuer url). The original url otherwise.
            """
            if (url is not None and
                    # and it's an Okta oauth2 URL
                    re.search('^http(s)?:\/\/.*\.okta\.com\/oauth2\/.+', url, flags=re.IGNORECASE) is not None and
                    # and it's missing the token suffix
                    re.search('\/v\d+\/token$', url, flags=re.IGNORECASE) is None):
                return url.rstrip('/') + '/v1/token'
            return url

        self.__token_url = format_token_url(value)

    @property
    def api_url(self):
        return self.__api_url

    @api_url.setter
    def api_url(self, value):
        self.__api_url = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def client_secret(self):
        return self.__client_secret

    @client_secret.setter
    def client_secret(self, value):
        self.__client_secret = value

    @property
    def app_name(self):
        return self.__app_name

    @app_name.setter
    def app_name(self, value):
        self.__app_name = value

    @property
    def certificate_filename(self):
        return self.__certificate_filename

    @certificate_filename.setter
    def certificate_filename(self, value):
        self.__certificate_filename = value

    @property
    def proxy_config(self):
        return self.__proxy_config

    @proxy_config.setter
    def proxy_config(self, value):
        self.__proxy_config = value

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value

