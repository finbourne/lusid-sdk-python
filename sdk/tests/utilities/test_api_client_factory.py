import unittest
from collections import UserString
from datetime import datetime
from unittest.mock import patch
from parameterized import parameterized

from lusid import ScopesApi, ResourceListOfScopeDefinition
from lusid.utilities import ApiClientFactory

from utilities import TokenUtilities as tu, CredentialsSource
from utilities.temp_file_manager import TempFileManager


class UnknownApi:
    pass


class UnknownImpl:
    pass


source_config_details, config_keys = CredentialsSource.fetch_credentials(), CredentialsSource.fetch_config_keys()


class RefreshingToken(UserString):

    def __init__(self):
        token_data = {"expires": datetime.now(), "current_access_token": ""}

        def get_token():
            token_data["current_access_token"] = None
            return token_data["current_access_token"]

        self.access_token = get_token

    def __getattribute__(self, name):
        token = object.__getattribute__(self, "access_token")()
        if name == "data":
            return token
        return token.__getattribute__(name)


class ApiFactory(unittest.TestCase):
    def validate_api(self, api):
        result = api.list_scopes()
        self.assertIsNotNone(result)
        self.assertGreater(len(result.values), 0)
        self.assertIsInstance(result, ResourceListOfScopeDefinition)

    @parameterized.expand([
        ["Unknown API", UnknownApi, "unknown api: UnknownApi"],
        ["Unknown Implementation", UnknownImpl, "unknown api: UnknownImpl"]
    ])
    def test_get_unknown_api_throws_exception(self, _, api_to_build, error_message):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )

        with self.assertRaises(TypeError) as error:
            factory.build(api_to_build)
        self.assertEqual(error.exception.args[0], error_message)

    def test_get_api_with_token(self):
        token, refresh_token = tu.get_okta_tokens(CredentialsSource.secrets_path())
        factory = ApiClientFactory(
            token=token,
            api_url=source_config_details["api_url"],
            app_name=source_config_details["app_name"]
        )
        api = factory.build(ScopesApi)
        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

    def test_get_api_with_none_token(self):
        factory = ApiClientFactory(
            token=None,
            api_url=source_config_details["api_url"],
            app_name=source_config_details["app_name"],
            api_secrets_filename=CredentialsSource.secrets_path(),
        )
        api = factory.build(ScopesApi)
        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

    def test_get_api_with_str_none_token(self):
        factory = ApiClientFactory(
            token=RefreshingToken(),
            api_url=source_config_details["api_url"],
            app_name=source_config_details["app_name"],
            api_secrets_filename=CredentialsSource.secrets_path(),
        )
        api = factory.build(ScopesApi)
        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

    def test_get_api_with_token_url_as_env_var(self):
        token, refresh_token = tu.get_okta_tokens(CredentialsSource.secrets_path())
        with patch.dict('os.environ', {"FBN_LUSID_API_URL": source_config_details["api_url"]}, clear=True):
            factory = ApiClientFactory(
                token=token,
                app_name=source_config_details["app_name"])
        api = factory.build(ScopesApi)
        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

    def test_get_api_with_configuration(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(ScopesApi)
        self.assertIsInstance(api, ScopesApi)
        self.validate_api(api)

    def test_get_api_with_info(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(ScopesApi)

        self.assertIsInstance(api, ScopesApi)
        result = api.list_scopes(call_info=lambda r: print(r))

        self.assertIsNotNone(result)

    def test_get_info_with_invalid_param_throws_error(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(ScopesApi)
        self.assertIsInstance(api, ScopesApi)

        with self.assertRaises(ValueError) as error:
            api.list_scopes(call_info="invalid param")

        self.assertEqual(error.exception.args[0], "call_info value must be a lambda")

    def test_wrapped_method(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )

        wrapped_scopes_api = factory.build(ScopesApi)
        portfolio = ScopesApi(wrapped_scopes_api.api_client)

        self.assertEqual(portfolio.__doc__, wrapped_scopes_api.__doc__)
        self.assertEqual(portfolio.__module__, wrapped_scopes_api.__module__)
        self.assertDictEqual(portfolio.__dict__, wrapped_scopes_api.__dict__)

    def test_get_api_with_proxy_file(self):

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
        # Load the config
        factory = ApiClientFactory(api_secrets_filename=secrets_file.name)
        # Close and thus delete the temporary file
        TempFileManager.delete_temp_file(secrets_file)
        api = factory.build(ScopesApi)
        self.validate_api(api)

    def test_get_api_with_proxy_config(self):

        secrets = {
            "api": {
                config_keys[key]["config"]: value for key, value in source_config_details.items() if
                value is not None and "proxy" not in key
            }
        }

        secrets["api"].pop("clientCertificate", None)

        if source_config_details.get("proxy_address", None) is None:
            self.skipTest(f"missing proxy configuration")

        secrets_file = TempFileManager.create_temp_file(secrets)
        # Load the config
        with patch.dict('os.environ', {}, clear=True):
            factory = ApiClientFactory(
                api_secrets_filename=secrets_file.name,
                proxy_url=source_config_details["proxy_address"],
                proxy_username=source_config_details["proxy_username"],
                proxy_password=source_config_details["proxy_password"])

        # Close and thus delete the temporary file
        TempFileManager.delete_temp_file(secrets_file)
        api = factory.build(ScopesApi)
        self.validate_api(api)
