import requests
import base64
import threading
import time

from datetime import datetime
from datetime import timedelta
from collections import UserString
from urllib.request import pathname2url


class RefreshingToken(UserString):

    def __init__(self, api_configuration, expiry_offset=60, id_provider_response_handler=None):
        """
        Implementation of UserString that will automatically refresh the token value upon expiry

        :param ApiConfiguration api_configuration: The api configuration with all required values
        :param int expiry_offset: number of seconds before token expiry to refresh the token
        :param callable id_provider_response_handler: A handler taking the Requests.Response from the identity provider
        before it is consumed by the RefreshingToken, mutation of the Response is possible with this handler
        """

        self.token_data = {
            "expires": None,
            "access_token": None,
            "refresh_token": None
        }
        self.expiry_offset = expiry_offset
        self.api_configuration = api_configuration
        self.id_provider_response_handler = id_provider_response_handler
        self.refresh_func = self.get_refresh_token
        self.lock = threading.Lock()
        self.retry_count = 0
        self.retry_limit = 5
        self.backoff_base = 2

    def update_token_data(self, id_provider_json):
        """
        Updates the token data from a response from the identity provider

        :param id_provider_json: The JSON to use to update the token data
        """
        self.token_data["access_token"] = id_provider_json["access_token"]
        # Set the expiry just before the actual expiry to ensure no failed requests
        delta = timedelta(seconds=id_provider_json.get("expires_in", 3600) - self.expiry_offset)
        self.token_data["expires"] = datetime.utcnow() + delta
        self.token_data["refresh_token"] = id_provider_json["refresh_token"]

    def get_access_token(self):
        """
        Retrieves an access token from the identity provider using the credentials in the provided configuration

        :return: The retrieved access token
        """

        encoded_password = pathname2url(self.api_configuration.password)
        encoded_client_id = pathname2url(self.api_configuration.client_id)
        encoded_client_secret = pathname2url(self.api_configuration.client_secret)

        # Prepare our authentication request
        token_request_body = f"grant_type=password&username={self.api_configuration.username}" \
            f"&password={encoded_password}&scope=openid client groups offline_access" \
            f"&client_id={encoded_client_id}&client_secret={encoded_client_secret}"

        headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        # extra request args
        kwargs = {"headers": headers}

        if self.api_configuration.proxy_config is not None:
            kwargs["proxies"] = self.api_configuration.proxy_config.format_proxy_schema()

        # use certificate if supplied
        if self.api_configuration.certificate_filename is not None:
            kwargs["verify"] = self.api_configuration.certificate_filename

        # make request to Okta to get an authentication token
        id_provider_response = requests.post(self.api_configuration.token_url, data=token_request_body, **kwargs)

        if self.id_provider_response_handler is not None:
            self.id_provider_response_handler(id_provider_response)

        # Ensure that we have a 200 response code
        if id_provider_response.status_code == 429:
            self._handle_retry(id_provider_response)
            return self.get_access_token()
        elif id_provider_response.status_code != 200:
            raise ValueError(id_provider_response.json())

        self.retry_count = 0

        # convert the json encoded response to be able to extract the token values
        id_provider_json = id_provider_response.json()

        self.update_token_data(id_provider_json)

        return self.token_data["access_token"]

    def get_refresh_token(self):
        """
        Retrieves an access token from the identity provider using the refresh token

        :return: The retrieved access token
        """

        # If any data is missing to use a refresh token e.g. on first try, get an access token using credentials
        if self.token_data["access_token"] is None or self.token_data["expires"] is None or self.token_data["refresh_token"] is None:
            return self.get_access_token()

        # check if the token has expired and refresh if needed
        if self.token_data["expires"] <= datetime.utcnow():

            encoded_client = base64.b64encode(bytes(f"{self.api_configuration.client_id}:{self.api_configuration.client_secret}", 'utf-8'))

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {encoded_client.decode('utf-8')}"
            }

            request_body = f"grant_type=refresh_token&scope=openid client groups offline_access&refresh_token={self.token_data['refresh_token']}"

            # request parameters
            kwargs = {"headers": headers}

            if self.api_configuration.proxy_config is not None:
                kwargs["proxies"] = self.api_configuration.proxy_config.format_proxy_schema()

            if self.api_configuration.certificate_filename is not None:
                kwargs["verify"] = self.api_configuration.certificate_filename

            id_provider_response = requests.post(self.api_configuration.token_url, data=request_body, **kwargs)

            if self.id_provider_response_handler is not None:
                self.id_provider_response_handler(id_provider_response)

            # Refresh token may be expired, if so, get new request token
            if id_provider_response.status_code == 400 and 'refresh token is invalid or expired' \
                    in id_provider_response.json()['error_description']:
                return self.get_access_token()
            elif id_provider_response.status_code == 429:
                self._handle_retry(id_provider_response)
                return self.get_refresh_token()
            elif id_provider_response.status_code != 200:
                raise ValueError(id_provider_response.json())

            self.retry_count = 0

            id_provider_json = id_provider_response.json()

            self.update_token_data(id_provider_json)

        return self.token_data["access_token"]

    def _handle_retry(self, id_provider_response):
        """
        Determines how to handle retrying in the event of a failed response. Currently uses the HTTP "Retry-After"
        header to determine how long to wait before retrying. If this header is not present defaults to a simple
        exponential back-off strategy.

        If the identity provider that you are interacting with does not provide a "Retry-After" header but does provide
        other custom headers, you can pass an id_provider_response_handler to the RefreshingToken which constructs
        the "Retry-After" header from the custom headers.

        :param requests.Response id_provider_response: The response from the identity provider
        """
        if self.retry_count >= self.retry_limit:
            raise ValueError(f"Max retry limit of {self.retry_limit} reached with response of {id_provider_response.json()}")

        self.retry_count += 1

        if "Retry-After" in id_provider_response.headers:
            retry_value = id_provider_response.headers.get("Retry-After")

            # Can be a delay in seconds or http date (https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After)
            try:
                wait_time = int(retry_value)
            except ValueError:
                # http date always in GMT
                wait_time = int(datetime.strptime(retry_value, '%a, %d %b %Y %H:%M:%S GMT').timestamp() - datetime.utcnow().timestamp())
                if wait_time <= 0:  # Won't wait for a negative period
                    return

            time.sleep(wait_time)
            return

        # If no "Retry-After" header implement a simple exponential back-off
        time.sleep(self._calculate_backoff(self.backoff_base, self.retry_count))

    @staticmethod
    def _calculate_backoff(backoff_base, retries):
        """
        Calculates the time to wait before retrying

        :param int retries: The number of retries attempted so far
        :param int backoff_base: The base to use for calculating the backoff

        :return: int: The number of seconds to wait
        """
        return backoff_base ** retries

    def __getattribute__(self, item):

        # return the value of the string
        if item == "data":
            self.lock.acquire()
            # check if the token has expired and go through the refresh token logic if it has
            token = object.__getattribute__(self, "refresh_func")()
            self.lock.release()
            return token

        # get the class attribute to be string class instead of the RefreshingToken class itself, used for UserString
        # base methods such as string concatenation, if this is missing the whole RefreshingToken class gets created
        # again with the concatenated string as the input, with this it creates a string instead
        if item == "__class__":
            return str

        # used to get .self attributes on the RefreshingToken
        return object.__getattribute__(self, item)
