from urllib3 import make_headers
from urllib.request import pathname2url
import requests

from lusid import Configuration, ApiClient

from .api_configuration_loader import ApiConfigurationLoader
from .refreshing_token import RefreshingToken


class ApiClientBuilder:
    """
    The ApiClientBuilder is responsible for building a lusid.ApiClient. This includes obtaining an access token from
    Okta or using the provided token.

    Any validation on the inputs required to build a lusid.ApiClient is the responsibility of this ApiClientBuilder.
    """

    @staticmethod
    def __check_required_fields(object_to_check, fields):
        """
        This function checks that the provided fields on an object are populated with values other than None

        :param object_to_check: The object to check the fields (a.k.a attributes) of
        :param list[str] fields: The fields to check on the object

        :return: None
        """
        # Check for fields which have a value of None
        missing_fields = [field for field in fields if getattr(object_to_check, field) is None]

        # Raise an error if any fields have a value of None
        if len(missing_fields) > 0:
            raise ValueError(
                f"The fields {str(missing_fields)} on the {object_to_check.__class__.__name__} are set to None, "
                f"please ensure that you have provided them directly, via a secrets file or environment "
                f"variables")

    @staticmethod
    def __generate_access_token(configuration, okta_response_handler):
        """
        This function generates an access token by making a call to Okta

        :param ApiConfiguration configuration: The configuration to use
        :param typing.callable okta_response_handler: An optional function to handle the Okta response

        :return: RefreshingToken api_token: A refreshing API token
        """
        # Encode credentials that may contain special characters
        encoded_password = pathname2url(configuration.password)
        encoded_client_id = pathname2url(configuration.client_id)
        encoded_client_secret = pathname2url(configuration.client_secret)

        # Prepare our authentication request
        token_request_body = f"grant_type=password&username={configuration.username}" \
            f"&password={encoded_password}&scope=openid client groups offline_access" \
            f"&client_id={encoded_client_id}&client_secret={encoded_client_secret}"

        headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        # extra request args
        kwargs = {"headers": headers}

        if configuration.proxy_config is not None:
            kwargs["proxies"] = configuration.proxy_config.format_proxy_schema()

        # use certificate if supplied
        if configuration.certificate_filename is not None:
            kwargs["verify"] = configuration.certificate_filename

        # make request to Okta to get an authentication token
        okta_response = requests.post(configuration.token_url, data=token_request_body, **kwargs)

        if okta_response_handler is not None:
            okta_response_handler(okta_response)

        # Ensure that we have a 200 response code
        if okta_response.status_code != 200:
            raise ValueError(okta_response.json())

        # convert the json encoded response to be able to extract the token values
        okta_json = okta_response.json()

        # Retrieve our api token from the authentication response
        api_token = RefreshingToken(token_url=configuration.token_url,
                                    client_id=encoded_client_id,
                                    client_secret=encoded_client_secret,
                                    initial_access_token=okta_json["access_token"],
                                    initial_token_expiry=okta_json["expires_in"],
                                    refresh_token=okta_json["refresh_token"],
                                    proxies=kwargs.get("proxies", None),
                                    certificate_filename=kwargs.get("verify", None))

        return api_token

    @classmethod
    def build(cls, api_secrets_filename=None, okta_response_handler=None, api_configuration=None, token=None):
        """
        :param str api_secrets_filename: The full path to the JSON file containing the API credentials and optional proxy details
        :param typing.callable okta_response_handler: An optional function to handle the Okta response
        :param lusid.utilities.ApiConfiguration api_configuration: A pre-populated ApiConfiguration
        :param str token: The pre-populated access token to use instead of asking Okta for a token

        :return: lusid.ApiClient: The configured LUSID ApiClient
        """

        # Load the configuration
        configuration = ApiConfigurationLoader.load(api_secrets_filename)

        # If an api_configuration has been provided override the loaded configuration with any properties that it has
        if api_configuration is not None:
            for key, value in vars(api_configuration).items():
                if value is not None:
                    setattr(configuration, key, value)

        # Use the access token provided if it exists
        if token is not None:
            # Check that there is an api_url available
            cls.__check_required_fields(configuration, ["api_url"])
            api_token = token
        # Otherwise generate an access token from Okta and use a RefreshingToken going forward
        else:
            # Check that all the required fields for generating a token exist
            cls.__check_required_fields(configuration, [
                "api_url",
                "password",
                "username",
                "client_id",
                "client_secret",
                "token_url"])

            # Generate an access token
            api_token = cls.__generate_access_token(
                configuration=configuration,
                okta_response_handler=okta_response_handler
            )

        # Initialise the API client using the token so that it can be included in all future requests
        config = Configuration()
        config.access_token = api_token
        config.host = configuration.api_url

        # Set the certificate from the configuration
        config.ssl_ca_cert = configuration.certificate_filename

        # Set the proxy for LUSID if needed
        if configuration.proxy_config is not None:
            config.proxy = configuration.proxy_config.address
            if configuration.proxy_config.username is not None and configuration.proxy_config.password is not None:
                config.proxy_headers = make_headers(
                    proxy_basic_auth=f"{configuration.proxy_config.username}:{configuration.proxy_config.password}"
                )

        # Create and return the ApiClient
        return ApiClient(
            configuration=config,
            header_name="X-LUSID-Application" if configuration.app_name is not None else None,
            header_value=configuration.app_name)
