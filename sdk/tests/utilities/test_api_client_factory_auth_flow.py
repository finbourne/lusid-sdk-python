import unittest
from unittest.mock import patch

from lusid import InstrumentsApi, ResourceListOfInstrumentIdTypeDescriptor, ApiException
from lusid.utilities import ApiClientFactory
from utilities import CredentialsSource


class ApiFactory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        cls.secrets = CredentialsSource.secrets_path()
        cls.os_environ_dict_str = 'os.environ'

        cls.source_config_details, cls.config_keys = CredentialsSource.fetch_credentials(), CredentialsSource.fetch_config_keys()
        cls.pat_token = CredentialsSource.fetch_pat()

    def validate_api(self, api):
        result = api.get_instrument_identifier_types()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ResourceListOfInstrumentIdTypeDescriptor)
        self.assertGreater(len(result.values), 0)

    def get_pat_env_var(self):

        pat_env_vars = {
            "FBN_LUSID_API_URL": self.source_config_details["api_url"],
            "FBN_LUSID_ACCESS_TOKEN": self.pat_token
        }

        return pat_env_vars

    def get_env_vars_without_pat(self):
        env_vars = {self.config_keys[key]["env"]: value for key, value in self.source_config_details.items() if
                    value is not None}
        env_vars_wout_pat = {k: env_vars[k] for k in env_vars if k != "FBN_LUSID_ACCESS_TOKEN"}
        return env_vars_wout_pat

    def test_bad_pat_in_param_but_good_pat_in_env_vars(self):

        with patch.dict(self.os_environ_dict_str, self.get_pat_env_var(), clear=True):

            try:

                factory = ApiClientFactory(token="INVALID_TOKEN")
                api = factory.build(InstrumentsApi)
                api.get_instrument_identifier_types()

            except ApiException as e:

                self.assertEquals(401, e.status)

    def test_bad_secrets_file_in_param_but_good_pat_in_env_vars(self):

        all_env_vars = self.get_env_vars_without_pat()
        all_env_vars["FBN_LUSID_ACCESS_TOKEN"] = self.pat_token

        with patch.dict(self.os_environ_dict_str, all_env_vars, clear=True):
            with self.assertLogs() as context_manager:
                import logging
                logger = logging.getLogger()
                logger.setLevel(logging.DEBUG)

                ApiClientFactory(api_secrets_filename="secrets_file_not_exist.json")

                self.assertEqual(
                    f"DEBUG:root:Provided secrets file of secrets_file_not_exist.json can not be found, please ensure you have correctly specified the full path to the file or don't provide a secrets file to use environment variables instead.",
                    context_manager.output[1],
                )

    def test_good_env_pat_but_no_param_pat(self):

        with patch.dict(self.os_environ_dict_str, self.get_pat_env_var(), clear=True):
            factory = ApiClientFactory()
            api = factory.build(InstrumentsApi)
            self.assertIsInstance(api, InstrumentsApi)
            self.validate_api(api)

    def test_no_env_pat_but_good_param_pat(self):

        with patch.dict(self.os_environ_dict_str, {"FBN_LUSID_API_URL": self.source_config_details["api_url"]},
                        clear=True):
            factory = ApiClientFactory(token=self.pat_token)
            api = factory.build(InstrumentsApi)
            self.assertIsInstance(api, InstrumentsApi)
            self.validate_api(api)

    def test_no_pat_but_good_secrets_file_as_param(self):

        with patch.dict(self.os_environ_dict_str, self.get_env_vars_without_pat(), clear=True):
            factory = ApiClientFactory(api_secrets_filename=self.secrets)
            api = factory.build(InstrumentsApi)
            self.assertIsInstance(api, InstrumentsApi)
            self.validate_api(api)

    def test_none_str_param_pat_but_good_secrets_envs(self):

        with patch.dict(self.os_environ_dict_str, self.get_env_vars_without_pat(), clear=True):
            factory = ApiClientFactory(token="None")
            api = factory.build(InstrumentsApi)
            self.assertIsInstance(api, InstrumentsApi)
            self.validate_api(api)

    def test_none_param_pat_but_good_secrets_envs(self):

        with patch.dict(self.os_environ_dict_str, self.get_env_vars_without_pat(), clear=True):
            factory = ApiClientFactory(token=None)
            api = factory.build(InstrumentsApi)
            self.assertIsInstance(api, InstrumentsApi)
            self.validate_api(api)

    def test_none_secrets_param_but_good_env_pat(self):

        with patch.dict(self.os_environ_dict_str, self.get_pat_env_var(), clear=True):
            factory = ApiClientFactory(api_secrets_filename=None)
            api = factory.build(InstrumentsApi)
            self.assertIsInstance(api, InstrumentsApi)
            self.validate_api(api)
