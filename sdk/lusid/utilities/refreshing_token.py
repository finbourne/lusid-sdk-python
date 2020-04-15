import requests
import base64

from datetime import datetime
from datetime import timedelta
from collections import UserString


class RefreshingToken(UserString):

    def __init__(self, token_url, client_id, client_secret, initial_access_token, initial_token_expiry, refresh_token,
                 expiry_offset=60, proxies=None, certificate_filename=None):
        """
        Implementation of UserString that will automatically refresh the token value upon expiry

        :param str token_url: token refresh url
        :param str client_id: OpenID Connect Client ID
        :param str client_secret: OpenID Connect Client Secret
        :param str initial_access_token: initial access token
        :param int initial_token_expiry: number of seconds the initial token is valid for before expiring
        :param str refresh_token: initial refresh token
        :param int expiry_offset: number of seconds before token expiry to refresh the token
        :param dict proxies: dictionary containing proxy schemas
        :param str certifiate_filename: The path to the client side certificate to use
        """

        token_data = {
            "expires": datetime.utcnow() + timedelta(seconds=initial_token_expiry),
            "access_token": initial_access_token
        }

        def get_refresh_token():

            # check if the token has expired and refresh if needed
            if token_data["expires"] <= datetime.utcnow():

                encoded_client = base64.b64encode(bytes(f"{client_id}:{client_secret}", 'utf-8'))

                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": f"Basic {encoded_client.decode('utf-8')}"
                }

                request_body = f"grant_type=refresh_token&scope=openid client groups offline_access&refresh_token={refresh_token}"

                # request parameters
                kwargs = {"headers": headers}
                kwargs["proxies"] = proxies
                kwargs["verify"] = certificate_filename

                okta_response = requests.post(token_url, data=request_body, **kwargs)

                if okta_response.status_code != 200:
                    raise Exception(okta_response.json())

                okta_json = okta_response.json()

                # set the expiry just before the actual expiry to be able to refresh in time
                delta = timedelta(seconds=okta_json.get("expires_in", 3600) - expiry_offset)
                token_data["expires"] = datetime.utcnow() + delta
                token_data["access_token"] = okta_json["access_token"]

            return token_data["access_token"]

        self.refresh_func = get_refresh_token

    def __getattribute__(self, item):

        token = object.__getattribute__(self, "refresh_func")()

        # return the value of the string
        if item == "data":
            return token

        return token.__getattribute__(item)
