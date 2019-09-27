class ApiConfiguration:

    def __init__(self, token_url, api_url, username, password, client_id, client_secret, app_name):
        self._token_url = token_url
        self._api_url = api_url
        self._username = username
        self._password = password
        self._client_id = client_id
        self._client_secret = client_secret
        self._app_name = app_name

    @property
    def token_url(self):
        return self._token_url

    @token_url.setter
    def token_url(self, value):
        self._token_url = value

    @property
    def api_url(self):
        return self._api_url

    @api_url.setter
    def api_url(self, value):
        self._api_url = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value):
        self._client_secret = value

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
