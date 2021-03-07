import unittest
from unittest.mock import patch
from parameterized import parameterized

from lusid import ApiClient
from lusid.utilities import ApiClientBuilder, ApiConfiguration
from lusid.utilities.proxy_config import ProxyConfig

from utilities import CredentialsSource
from utilities.temp_file_manager import TempFileManager

source_config_details, config_keys = CredentialsSource.fetch_credentials(), CredentialsSource.fetch_config_keys()


class ApiClientBuilderTests(unittest.TestCase):

    # reused string literals
    OS_ENVIRON = "os.environ"
    REQUESTS_POST = "requests.post"

    # Test creation with configuration inc proxy settings

    @parameterized.expand(
        [
            [
                "Missing api_url when using an explicit token",
                ["api_url"],
                "example_token"
            ],
            [
                "Missing username and password when generating a token",
                ["password", "username"],
                None
            ]
        ], testcase_func_name=CredentialsSource.custom_name_func
    )
    def test_missing_from_config_file_throws(self, _, missing_attributes, token):
        """
        Tests that if some required fields are missing from the ApiConfiguration an error is thrown

        :return:
        """
        # Create an ApiConfiguration with all values populated
        proxy_config = ProxyConfig(**{
            key.replace("proxy_", ""): value for key, value in source_config_details.items() if value is not None and "proxy" in key
        }) if source_config_details["proxy_address"] is not None else None

        api_config_kwargs = {key: value for key, value in source_config_details.items() if value is not None and "proxy" not in key}
        api_config_kwargs["proxy_config"] = proxy_config
        api_configuration = ApiConfiguration(**api_config_kwargs)

        # Pop off the missing attributes
        [setattr(api_configuration, missing_attribute, None) for missing_attribute in missing_attributes]

        # Ensure that there are no environment variables which can be used to fill the missing Api Url
        with patch.dict('os.environ', clear=True), self.assertRaises(ValueError) as ex:
            ApiClientBuilder.build(api_configuration=api_configuration, token=token)

        self.assertEqual(
            ex.exception.args[0], f"The fields {str(missing_attributes)} on the ApiConfiguration are set to None, "
                                  f"please ensure that you have provided them directly, via a secrets file or environment "
                                  f"variables")

    def test_build_client_no_token_provided_config_takes_precedence(self):
        """
        This test builds an ApiClient from a provided secrets.json file. The call to generate the token is mocked here.
        """

        secrets = {
                    "api": {
                        config_keys[key]["config"]: "DUMMYVALUE" for key in source_config_details.keys() if
                        "proxy" not in key
                    }
                }

        env_vars = {}

        api_configuration = ApiConfiguration(**{
                    key: value for key, value in source_config_details.items() if "proxy" not in key
        })

        # Use a temporary file and no environment variables to generate the API Client
        with patch.dict('os.environ', env_vars, clear=True), patch(self.REQUESTS_POST) as mock_requests:

            mock_requests.return_value.status_code = 200
            mock_requests.return_value.json.return_value = {
                "access_token": "mock_access_token",
                "refresh_token": "mock_refresh_token",
                "expires_in": 60
            }

            secrets_file = TempFileManager.create_temp_file(secrets)
            client = ApiClientBuilder.build(
                api_secrets_filename=secrets_file.name,
                api_configuration=api_configuration)

            TempFileManager.delete_temp_file(secrets_file)

        self.assertEqual(client.configuration.host, source_config_details["api_url"])
        self.assertEqual(client.configuration.access_token, "mock_access_token")
        self.assertIsInstance(client, ApiClient)

    def test_build_client_no_token_provided_file_only(self):
        """
        This test builds an ApiClient from a provided secrets.json file. The call to generate the token is mocked here.
        """

        secrets = {
                    "api": {
                        config_keys[key]["config"]: value for key, value in source_config_details.items() if
                        value is not None and "proxy" not in key
                    }
                }

        env_vars = {}

        api_configuration = None

        # Use a temporary file and no environment variables to generate the API Client
        with patch.dict('os.environ', env_vars, clear=True), patch(self.REQUESTS_POST) as mock_requests:

            mock_requests.return_value.status_code = 200
            mock_requests.return_value.json.return_value = {
                "access_token": "mock_access_token",
                "refresh_token": "mock_refresh_token",
                "expires_in": 60
            }

            secrets_file = TempFileManager.create_temp_file(secrets)
            client = ApiClientBuilder.build(
                api_secrets_filename=secrets_file.name,
                api_configuration=api_configuration)

            TempFileManager.delete_temp_file(secrets_file)

        self.assertEqual(client.configuration.host, source_config_details["api_url"])
        self.assertEqual(client.configuration.access_token, "mock_access_token")
        self.assertIsInstance(client, ApiClient)

    @parameterized.expand(
        [
            [
                "Build client from token ONLY",
                ["api"],
                {},
                ApiConfiguration(
                    api_url=source_config_details["api_url"]),
                "abc42123.e423klfkel.sdlj53kl23423"
            ],
            [
                "Test that when token and secrets file are provided the token is used",
                [],
                {},
                None,
                "abc42123.e423klfkel.sdlj53kl23423"
            ],
        ], testcase_func_name=CredentialsSource.custom_name_func
    )
    def test_build_client_with_token_provided(self, _, config_to_remove, env_vars, api_configuration, token):
        """
        This test builds an ApiClient from a provided token.
        """

        secrets = {
            "api": {
                config_keys[key]["config"]: value for key, value in source_config_details.items() if
                value is not None and "proxy" not in key
            }
        }

        [secrets.pop(config) for config in config_to_remove]

        # Use a temporary file and no environment variables to generate the API Client
        with patch.dict('os.environ', env_vars, clear=True):

            secrets_file = TempFileManager.create_temp_file(secrets)
            client = ApiClientBuilder.build(
                api_secrets_filename=secrets_file.name,
                api_configuration=api_configuration,
                token=token)

            TempFileManager.delete_temp_file(secrets_file)

        self.assertEqual(client.configuration.host, source_config_details["api_url"])
        self.assertEqual(client.configuration.access_token, token)
        self.assertIsInstance(client, ApiClient)

    def test_use_okta_response_handler(self):

        api_configuration = ApiConfiguration(**{
            key: value for key, value in source_config_details.items() if "proxy" not in key
        })

        api_configuration.certificate_filename = None

        env_vars = {}

        def response_handler(okta_response):
            if not okta_response.json.return_value.get("refresh_token", False):
                raise ValueError("Refresh token missing from config")

        with patch.dict('os.environ', env_vars, clear=True), patch(self.REQUESTS_POST) as mock_requests, self.assertRaises(ValueError):

            mock_requests.return_value.status_code = 200
            mock_requests.return_value.json.return_value = {
                "access_token": "mock_access_token",
                "expires_in": 60
            }

            ApiClientBuilder.build(
                api_configuration=api_configuration,
                okta_response_handler=response_handler)

