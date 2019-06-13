import os
import requests
import lusid
import json

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class ApiClientBuilder:

    def build(self, api_configuration):
        """
        :param api_configuration: name api configuration file
        :return: ApiClient correctly configured with credentials and host
        """

        # Load our configuration details from the environment variables
        token_url = os.getenv("FBN_TOKEN_URL", None)
        api_url = os.getenv("FBN_LUSID_API_URL", None)
        username = os.getenv("FBN_USERNAME", None)
        password_raw = os.getenv("FBN_PASSWORD", None)
        client_id_raw = os.getenv("FBN_CLIENT_ID", None)
        client_secret_raw = os.getenv("FBN_CLIENT_SECRET", None)

        # If any of the environmental variables are missing use a local secrets file
        if token_url is None or username is None or password_raw is None or client_id_raw is None \
                or client_secret_raw is None or api_url is None:

            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(os.path.join(dir_path, api_configuration), "r") as secrets:
                config = json.load(secrets)

            token_url = os.getenv("FBN_TOKEN_URL", config["api"]["tokenUrl"])
            username = os.getenv("FBN_USERNAME", config["api"]["username"])
            password = pathname2url(os.getenv("FBN_PASSWORD", config["api"]["password"]))
            client_id = pathname2url(os.getenv("FBN_CLIENT_ID", config["api"]["clientId"]))
            client_secret = pathname2url(os.getenv("FBN_CLIENT_SECRET", config["api"]["clientSecret"]))
            api_url = os.getenv("FBN_LUSID_API_URL", config["api"]["apiUrl"])

        else:
            password = pathname2url(password_raw)
            client_id = pathname2url(client_id_raw)
            client_secret = pathname2url(client_secret_raw)

        # Prepare our authentication request
        token_request_body = ("grant_type=password&username={0}".format(username) +
                              "&password={0}&scope=openid client groups".format(password) +
                              "&client_id={0}&client_secret={1}".format(client_id, client_secret))
        headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        # Make our authentication request
        okta_response = requests.post(token_url, data=token_request_body, headers=headers)

        # Ensure that we have a 200 response code
        assert okta_response.status_code == 200

        # Retrieve our api token from the authentication response
        api_token = okta_response.json()["access_token"]

        # Initialise our API client using our token so that we can include it in all future requests
        config = lusid.Configuration()
        config.access_token = api_token
        config.host = api_url

        return lusid.ApiClient(config)


