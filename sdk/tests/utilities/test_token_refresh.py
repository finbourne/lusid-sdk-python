import os
import unittest
from time import sleep

from lusid.utilities import ApiConfigurationLoader
from lusid.utilities.proxy_config import ProxyConfig
from lusid.utilities import RefreshingToken

from utilities import CredentialsSource
from unittest.mock import patch
from utilities import TokenUtilities as tu
from utilities.temp_file_manager import TempFileManager

source_config_details, config_keys = CredentialsSource.fetch_credentials(), CredentialsSource.fetch_config_keys()


class TokenRefresh(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())

    def test_get_token(self):
        original_token, refresh_token = tu.get_okta_tokens(CredentialsSource.secrets_path())

        refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                          client_id=self.config.client_id,
                                          client_secret=self.config.client_secret,
                                          initial_access_token=original_token,
                                          initial_token_expiry=3600,
                                          refresh_token=refresh_token)

        self.assertIsNotNone(refreshed_token)
        self.assertEqual(original_token, refreshed_token)

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

        secrets_file = TempFileManager.create_temp_file(secrets)

        original_token, refresh_token = tu.get_okta_tokens(secrets_file.name)

        proxy_config = ProxyConfig(
            address=secrets["proxy"]["address"],
            username=secrets["proxy"]["username"],
            password=secrets["proxy"]["password"]
        )

        proxies = proxy_config.format_proxy_schema()

        with patch.dict('os.environ', {"HTTPS_PROXY": proxies["https"]}, clear=True):
            proxy_url = os.getenv("HTTPS_PROXY", None)

        if proxy_url is not None:

            refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                              client_id=self.config.client_id,
                                              client_secret=self.config.client_secret,
                                              initial_access_token=original_token,
                                              initial_token_expiry=1,  # 1s expiry
                                              refresh_token=refresh_token,
                                              expiry_offset=3599,     # set to 1s expiry
                                              proxies={})

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

        secrets_file = TempFileManager.create_temp_file(secrets)

        original_token, refresh_token = tu.get_okta_tokens(secrets_file.name)

        proxy_config = ProxyConfig(
            address=secrets["proxy"]["address"],
            username=secrets["proxy"]["username"],
            password=secrets["proxy"]["password"]
        )

        proxies = proxy_config.format_proxy_schema()

        refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                          client_id=self.config.client_id,
                                          client_secret=self.config.client_secret,
                                          initial_access_token=original_token,
                                          initial_token_expiry=1,  # 1s expiry
                                          refresh_token=refresh_token,
                                          expiry_offset=3599,     # set to 1s expiry
                                          proxies=proxies)

        self.assertIsNotNone(refreshed_token)


    def test_refreshed_token_when_expired(self):
        original_token, refresh_token = tu.get_okta_tokens(CredentialsSource.secrets_path())

        refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                          client_id=self.config.client_id,
                                          client_secret=self.config.client_secret,
                                          initial_access_token=original_token,
                                          initial_token_expiry=1,  # 1s expiry
                                          refresh_token=refresh_token,
                                          expiry_offset=3599)  # set to 1s expiry

        self.assertIsNotNone(refreshed_token)

        # force de-referencing the token value
        first_value = f"{refreshed_token}"

        sleep(1)

        self.assertNotEqual(first_value, refreshed_token)

    def test_token_when_not_expired_does_not_refresh(self):
        original_token, refresh_token = tu.get_okta_tokens(CredentialsSource.secrets_path())

        refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                          client_id=self.config.client_id,
                                          client_secret=self.config.client_secret,
                                          initial_access_token=original_token,
                                          initial_token_expiry=3600,
                                          refresh_token=refresh_token)

        self.assertIsNotNone(refreshed_token)

        # force de-referencing the token value
        first_value = f"{refreshed_token}"

        sleep(1)

        self.assertEqual(first_value, refreshed_token)

    def test_can_make_header(self):
        original_token, refresh_token = tu.get_okta_tokens(CredentialsSource.secrets_path())

        refreshed_token = RefreshingToken(token_url=self.config.token_url,
                                          client_id=self.config.client_id,
                                          client_secret=self.config.client_secret,
                                          initial_access_token=original_token,
                                          initial_token_expiry=3600,
                                          refresh_token=refresh_token)

        header = "Bearer " + refreshed_token

        self.assertIsNotNone(header)
