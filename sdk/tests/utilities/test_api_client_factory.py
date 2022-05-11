import unittest
from collections import UserString
from datetime import datetime
from unittest.mock import patch
from urllib3 import PoolManager, ProxyManager
from parameterized import parameterized
from threading import Thread
from lusid import (InstrumentsApi, ResourceListOfInstrumentIdTypeDescriptor,
                   TCPKeepAlivePoolManager, TCPKeepAliveProxyManager)
from lusid.utilities import ApiClientFactory

from utilities import TokenUtilities as tu, CredentialsSource
from utilities.temp_file_manager import TempFileManager
from utilities import MockApiResponse


class UnknownApi:
    pass


class UnknownImpl:
    pass


source_config_details, config_keys = CredentialsSource.fetch_credentials(), CredentialsSource.fetch_config_keys()
pat_token = CredentialsSource.fetch_pat()

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

    def get_env_vars_without_pat(self):
        env_vars = {config_keys[key]["env"]: value for key, value in source_config_details.items()if value is not None}
        env_vars_without_pat = {k:env_vars[k] for k in env_vars if k !="FBN_LUSID_ACCESS_TOKEN"}
        return env_vars_without_pat

    def validate_api(self, api):
        result = api.get_instrument_identifier_types()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ResourceListOfInstrumentIdTypeDescriptor)
        self.assertGreater(len(result.values), 0)

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
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_none_token(self):
        factory = ApiClientFactory(
            token=None,
            api_url=source_config_details["api_url"],
            app_name=source_config_details["app_name"],
            api_secrets_filename=CredentialsSource.secrets_path(),
        )
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_str_none_token(self):
        factory = ApiClientFactory(
            token=RefreshingToken(),
            api_url=source_config_details["api_url"],
            app_name=source_config_details["app_name"],
            api_secrets_filename=CredentialsSource.secrets_path(),
        )
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_token_url_as_env_var(self):
        token, refresh_token = tu.get_okta_tokens(CredentialsSource.secrets_path())
        with patch.dict('os.environ', {"FBN_LUSID_API_URL": source_config_details["api_url"]}, clear=True):
            factory = ApiClientFactory(
                token=token,
                app_name=source_config_details["app_name"])
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_configuration(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_info(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(InstrumentsApi)

        self.assertIsInstance(api, InstrumentsApi)
        result = api.get_instrument_identifier_types(call_info=lambda r: print(r))

        self.assertIsNotNone(result)

    def test_get_info_with_invalid_param_throws_error(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)

        with self.assertRaises(ValueError) as error:
            api.get_instrument_identifier_types(call_info="invalid param")

        self.assertEqual(error.exception.args[0], "call_info value must be a lambda")

    def test_wrapped_method(self):
        factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path()
        )

        wrapped_scopes_api = factory.build(InstrumentsApi)
        portfolio = InstrumentsApi(wrapped_scopes_api.api_client)

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
        api = factory.build(InstrumentsApi)
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
        api = factory.build(InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_correlation_id_from_env_var(self):

        env_vars = {config_keys[key]["env"]: value for key, value in source_config_details.items() if value is not None}
        env_vars["FBN_CORRELATION_ID"] = "env-correlation-id"

        with patch.dict('os.environ', env_vars, clear=True):
            factory = ApiClientFactory()
            api = factory.build(InstrumentsApi)
            self.assertIsInstance(api, InstrumentsApi)
            self.validate_api(api)
            self.assertTrue("CorrelationId" in api.api_client.default_headers, msg="CorrelationId not found in headers")
            self.assertEquals(api.api_client.default_headers["CorrelationId"], "env-correlation-id")

    def test_get_api_with_correlation_id_from_param(self):

        env_vars = {config_keys[key]["env"]: value for key, value in source_config_details.items() if value is not None}

        with patch.dict('os.environ', env_vars, clear=True):
            factory = ApiClientFactory(
                api_secrets_filename=CredentialsSource.secrets_path(),
                correlation_id="param-correlation-id"
            )
            api = factory.build(InstrumentsApi)
            self.assertIsInstance(api, InstrumentsApi)
            self.validate_api(api)
            self.assertTrue("CorrelationId" in api.api_client.default_headers, msg="CorrelationId not found in headers")
            self.assertEquals(api.api_client.default_headers["CorrelationId"], "param-correlation-id")

    def test_get_api_with_tcp_keep_alive(self):
        api_factory = ApiClientFactory(
            api_secrets_filename=CredentialsSource.secrets_path(),
            tcp_keep_alive=True
        )
        # Make sure tcp_keep_alive was passed through all of the layers
        self.assertTrue(api_factory.api_client.configuration.tcp_keep_alive)
        self.assertIsInstance(api_factory.api_client.rest_client.pool_manager,
                              (TCPKeepAlivePoolManager, TCPKeepAliveProxyManager))

    def test_get_api_without_tcp_keep_alive(self):
        api_factory = ApiClientFactory(api_secrets_filename=CredentialsSource.secrets_path())
        # Make sure tcp_keep_alive was passed through all of the layers
        self.assertFalse(api_factory.api_client.configuration.tcp_keep_alive)
        self.assertIsInstance(api_factory.api_client.rest_client.pool_manager, (PoolManager, ProxyManager))

    def test_use_apifactory_with_id_provider_response_handler(self):
        """
        Ensures that an id_provider_response handler that is passed to the ApiClientFactory can be used during
        communication with the id provider (if appropriate).
        """

        with patch.dict('os.environ', self.get_env_vars_without_pat(), clear=True):

            responses = []

            def record_response(id_provider_response):
                nonlocal responses
                responses.append(id_provider_response.status_code)

            api_factory = ApiClientFactory(
                api_secrets_filename=CredentialsSource.secrets_path(),
                id_provider_response_handler=record_response
            )

            api = api_factory.build(InstrumentsApi)
            self.validate_api(api)

            self.assertGreater(len(responses), 0)

    def test_use_apifactory_multiple_threads(self):

        with patch.dict('os.environ', self.get_env_vars_without_pat(), clear=True):

            access_token = str(ApiClientFactory(
                api_secrets_filename=CredentialsSource.secrets_path()
            ).api_client.configuration.access_token)

            api_factory = ApiClientFactory(
                api_secrets_filename=CredentialsSource.secrets_path()
            )

            def get_identifier_types(factory):
                return factory.build(InstrumentsApi).get_instrument_identifier_types()

            thread1 = Thread(target=get_identifier_types, args=[api_factory])
            thread2 = Thread(target=get_identifier_types, args=[api_factory])
            thread3 = Thread(target=get_identifier_types, args=[api_factory])

            with patch("requests.post") as identity_mock:
                identity_mock.side_effect = lambda *args, **kwargs: MockApiResponse(
                    json_data={
                        "access_token": f"{access_token}",
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