import unittest
from unittest.mock import patch
import inspect

from lusid import ApiConfigurationLoader
from lusid.utilities.api_configuration import ApiConfiguration
from lusid.utilities.proxy_config import ProxyConfig

from utilities import CredentialsSource
from utilities.temp_file_manager import TempFileManager

source_config_details, config_keys = CredentialsSource.fetch_credentials(), CredentialsSource.fetch_config_keys()


class ApiConfigurationLoaderTests(unittest.TestCase):
    """
    These test ensure that the ApiConfigurationLoader works as expected

    """
    def assert_config_values(self, config, secrets):
        """
        Not a test. This is used to test the values of the ApiConfiguration.

        :param lusid.utilities.ApiConfiguration config: The ApiConfiguration to test the values of
        :param dict secrets: A dictionary with the secrets using a common addressing scheme for both environment
        variables and secret file variables

        :return: None
        """
        # Use assertTrue to avoid leaking details when assertion fails
        for key, value in secrets.items():

            # If not a proxy configuration check against the ApiConfiguration
            if "proxy" not in key:
                self.assertTrue(getattr(config, key) == secrets[key])
            # Otherwise check against the ApiConfiguration.proxy_config
            elif config.proxy_config is None:
                self.assertTrue(secrets.get("proxy_address", None) is None)
            else:
                self.assertTrue(getattr(config.proxy_config, key.replace("proxy_", "")) == secrets[key])

    def test_config_file_preferred_over_env_vars(self):
        """
        This tests loading the configuration details in multiple different ways

        :return: None
        """

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

        env_vars = {config_keys[key]["env"]: "DUMMYVALUE" for key, value in source_config_details.items() if value is not None}

        # Set the environment variables as desired
        with patch.dict('os.environ', env_vars, clear=True):
            # Create a temporary secrets file as desired
            secrets_file = TempFileManager.create_temp_file(secrets)
            # Load the config
            config = ApiConfigurationLoader.load(secrets_file.name)
            # Close and thus delete the temporary file
            TempFileManager.delete_temp_file(secrets_file)
            # Ensure that the config is populated as expected
            self.assert_config_values(config, source_config_details)

    def test_missing_env_vars_uses_config_file(self):
        """
        This tests loading the configuration details in multiple different ways

        :return: None
        """

        secrets = {
            "api": {
                config_keys["token_url"]["config"]: source_config_details["token_url"]
            }
        }

        env_vars = {config_keys[key]["env"]: value for key, value in source_config_details.items() if
         value is not None and "token_url" not in key}

        # Set the environment variables as desired
        with patch.dict('os.environ', env_vars, clear=True):
            # Create a temporary secrets file as desired
            secrets_file = TempFileManager.create_temp_file(secrets)
            # Load the config
            config = ApiConfigurationLoader.load(secrets_file.name)
            # Close and thus delete the temporary file
            TempFileManager.delete_temp_file(secrets_file)
            # Ensure that the config is populated as expected
            self.assert_config_values(config, source_config_details)

    def test_missing_config_file_vars_uses_env_vars(self):
        """
        This tests loading the configuration details in multiple different ways

        :return: None
        """

        secrets = {
            "api": {
                config_keys[key]["config"]: value for key, value in source_config_details.items() if
                value is not None and "proxy" not in key
            },
            "proxy": {
                config_keys[key]["config"]: value for key, value in source_config_details.items() if
                value is not None and "proxy" in key and "token_url" not in key
            }
        }

        env_vars = {config_keys["token_url"]["env"]: source_config_details["token_url"]}

        # Set the environment variables as desired
        with patch.dict('os.environ', env_vars, clear=True):
            # Create a temporary secrets file as desired
            secrets_file = TempFileManager.create_temp_file(secrets)
            # Load the config
            config = ApiConfigurationLoader.load(secrets_file.name)
            # Close and thus delete the temporary file
            TempFileManager.delete_temp_file(secrets_file)
            # Ensure that the config is populated as expected
            self.assert_config_values(config, source_config_details)

    def test_load_from_config_file_only(self):
        """
        This tests loading the configuration details in multiple different ways

        :return: None
        """

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

        env_vars = {}

        # Set the environment variables as desired
        with patch.dict('os.environ', env_vars, clear=True):
            # Create a temporary secrets file as desired
            secrets_file = TempFileManager.create_temp_file(secrets)
            # Load the config
            config = ApiConfigurationLoader.load(secrets_file.name)
            # Close and thus delete the temporary file
            TempFileManager.delete_temp_file(secrets_file)
            # Ensure that the config is populated as expected
            self.assert_config_values(config, source_config_details)

    def test_load_from_environment_vars_only(self):
        """
        This tests loading all of the configuration details from environment variables ONLY.

        :return: None
        """
        # Set all the environment variables
        env_vars = {config_keys[key]["env"]: value for key, value in source_config_details.items() if value is not None}
        with patch.dict('os.environ', env_vars, clear=True):
            config = ApiConfigurationLoader.load()

        self.assert_config_values(config, source_config_details)

    @unittest.skip("Logging a warning instead of raising an exception")
    def test_specify_config_file_not_exist(self):
        """
        This test checks that an error is raised if a secrets file is specified which can not be found

        :return: None
        """
        non_existent_secrets_file = "Thisfiledefinitelydoesnotexist.json"

        with self.assertRaises(ValueError) as ex:
            ApiConfigurationLoader.load(non_existent_secrets_file)

        self.assertEqual(ex.exception.args[0], f"Provided secrets file of {non_existent_secrets_file} can not be found, please ensure you "
                             f"have correctly specified the full path to the file or don't provide a secrets file to use "
                             f"environment variables instead.")

    def test_config_keys_aligned(self):
        """
        This tests that the file containing the keys used to hold the values for the different credentials and proxy
        details in the secrets.json file and environment variables matches the attributes of the ProxyConfig and
        ApiConfiguration classes.

        This allows for the simple creation of these classes from environment variables or a secrets file. If this
        test fails it means that there will be problems creating instances of these classes in the ApiConfigurationLoader.

        It also allows for mapping between the name of an environment variable and its corresponding name in the secrets
        file and vice-versa.

        :return: None
        """

        # Get the set of keys for proxy settings and api credentials
        proxy_config_key_set = set([key.replace("proxy_", "") for key in config_keys.keys() if "proxy" in key])
        api_config_key_set = set([key for key in config_keys.keys() if "proxy" not in key])

        # Get the attributes on the ProxyConfig and ApiConfiguration Classes
        api_config_attributes = set([attribute[0] for attribute in inspect.getmembers(ApiConfiguration)])
        proxy_config_attributes = set([attribute[0] for attribute in inspect.getmembers(ProxyConfig)])

        # Ensure that the config file is a subset of the attributes on these classes to ensure seamless instance creation
        self.assertTrue(proxy_config_key_set.issubset(proxy_config_attributes))
        self.assertTrue(api_config_key_set.issubset(api_config_attributes))
