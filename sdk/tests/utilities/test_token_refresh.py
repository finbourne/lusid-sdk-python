import os
import unittest
from time import sleep
from threading import Thread

from lusid.utilities import ApiConfigurationLoader
from lusid.utilities.proxy_config import ProxyConfig
from lusid.utilities import RefreshingToken

from utilities import CredentialsSource
from unittest.mock import patch
from utilities.temp_file_manager import TempFileManager
from utilities import MockApiResponse

source_config_details, config_keys = CredentialsSource.fetch_credentials(), CredentialsSource.fetch_config_keys()


class TokenRefresh(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())

    def test_get_token(self):

        refreshed_token = RefreshingToken(api_configuration=self.config)
        self.assertIsNotNone(refreshed_token)

    def test_get_token_with_proxy(self):

        secrets = {
            "api": {
                config_keys[key]["config"]: value for key, value in source_config_details.items() if
                value is not None and "proxy" not in key
            },
            "proxy": {
                config_keys[key]["config"]: value for key, value in source_config_details.items() if
                value is not None and "proxy" in key
            }
        }

        secrets["api"].pop("clientCertificate", None)

        if secrets["proxy"].get("address", None) is None:
            self.skipTest(f"missing proxy configuration")

        TempFileManager.create_temp_file(secrets)

        proxy_config = ProxyConfig(
            address=secrets["proxy"]["address"],
            username=secrets["proxy"]["username"],
            password=secrets["proxy"]["password"]
        )

        proxies = proxy_config.format_proxy_schema()

        with patch.dict('os.environ', {"HTTPS_PROXY": proxies["https"]}, clear=True):
            proxy_url = os.getenv("HTTPS_PROXY", None)

        if proxy_url is not None:

            refreshed_token = RefreshingToken(api_configuration=self.config,
                                              expiry_offset=3599)

            self.assertIsNotNone(refreshed_token)

    def test_get_token_with_proxy_from_config(self):

        secrets = {
            "api": {
                config_keys[key]["config"]: value for key, value in source_config_details.items() if
                value is not None and "proxy" not in key
            },
            "proxy": {
                config_keys[key]["config"]: value for key, value in source_config_details.items() if
                value is not None and "proxy" in key
            }
        }

        secrets["api"].pop("clientCertificate", None)

        if secrets["proxy"].get("address", None) is None:
            self.skipTest(f"missing proxy configuration")

        TempFileManager.create_temp_file(secrets)

        refreshed_token = RefreshingToken(api_configuration=self.config,
                                          expiry_offset=3599)

        self.assertIsNotNone(refreshed_token)

    def test_refreshed_token_when_expired(self):

        refreshed_token = RefreshingToken(api_configuration=self.config,
                                          expiry_offset=3599)  # set to 1s expiry

        self.assertIsNotNone(refreshed_token)

        # force de-referencing the token value
        first_value = f"{refreshed_token}"

        sleep(1)

        self.assertNotEqual(first_value, refreshed_token)

    def test_token_when_refresh_token_expired_still_refreshes(self):

        refreshed_token = RefreshingToken(api_configuration=self.config, expiry_offset=3599)

        self.assertIsNotNone(refreshed_token)

        # force de-referencing the token value
        first_value = f"{refreshed_token}"

        sleep(1)

        with patch("requests.post", side_effect=[
            MockApiResponse(
                json_data={
                    "error": "invalid_grant",
                    "error_description": "The refresh token is invalid or expired."
                },
                status_code=400
            ),
            MockApiResponse(
                json_data={
                    "access_token": "mock_access_token",
                    "refresh_token": "mock_refresh_token",
                    "expires_in": 60
                },
                status_code=200
            ),
        ]):

            self.assertNotEqual(first_value, refreshed_token)

    def test_token_when_not_expired_does_not_refresh(self):

        refreshed_token = RefreshingToken(api_configuration=self.config)

        self.assertIsNotNone(refreshed_token)

        # force de-referencing the token value
        first_value = f"{refreshed_token}"

        sleep(1)

        self.assertEqual(first_value, refreshed_token)

    def test_can_make_header(self):

        refreshed_token = RefreshingToken(api_configuration=self.config)

        header = "Bearer " + refreshed_token

        self.assertIsNotNone(header)

    def test_use_refresh_token_multiple_threads(self):

        def force_refresh(refresh_token):
            return f"{refresh_token}"

        refreshed_token = RefreshingToken(api_configuration=self.config)

        thread1 = Thread(target=force_refresh, args=[refreshed_token])
        thread2 = Thread(target=force_refresh, args=[refreshed_token])
        thread3 = Thread(target=force_refresh, args=[refreshed_token])

        with patch("requests.post") as identity_mock:
            identity_mock.side_effect = lambda *args, **kwargs: MockApiResponse(
                json_data={
                    "access_token": "mock_access_token",
                    "refresh_token": "mock_refresh_token",
                    "expires_in": 3600
                },
                status_code=200
            )

            thread1.start()
            thread2.start()
            thread3.start()

            thread1.join()
            thread2.join()
            thread3.join()

            # Ensure that we only got an access token once
            self.assertEqual(1, identity_mock.call_count)
