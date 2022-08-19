import os
import unittest
from time import sleep, time
from threading import Thread
from datetime import datetime, timedelta

from lusid.utilities import ApiConfigurationLoader
from lusid.utilities.proxy_config import ProxyConfig
from lusid.utilities import RefreshingToken
from parameterized import parameterized

from utilities import CredentialsSource
from unittest.mock import patch
from utilities.temp_file_manager import TempFileManager
from utilities import MockApiResponse

source_config_details, config_keys = CredentialsSource.fetch_credentials(), CredentialsSource.fetch_config_keys()



@unittest.skipIf(CredentialsSource.fetch_credentials().__contains__("access_token"), "do not run on PR's")
class TokenRefresh(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())

    def test_get_token(self):

        refreshed_token = RefreshingToken(api_configuration=self.config)
        self.assertIsNotNone(refreshed_token)

    @staticmethod
    def force_refresh(refresh_token):
        return f"{refresh_token}"

    @staticmethod
    def convert_to_http_date(datetime_value):

        return datetime_value.strftime('%a, %d %b %Y %H:%M:%S GMT')

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

        refreshed_token = RefreshingToken(api_configuration=self.config)

        thread1 = Thread(target=self.force_refresh, args=[refreshed_token])
        thread2 = Thread(target=self.force_refresh, args=[refreshed_token])
        thread3 = Thread(target=self.force_refresh, args=[refreshed_token])

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

    def test_retries_on_429_status_code_initial_access_token(self):
        """
        Ensures that in the event of a 429 HTTP Status Code being returned when communicating with an identity
        provider, the request is retried.
        """

        refreshing_token = RefreshingToken(api_configuration=self.config)

        with patch("requests.post") as identity_mock:
            identity_mock.side_effect = [
                # Return a 429 on the first attempt
                MockApiResponse(
                    json_data={
                        "error": "rate_limit",
                        "error_description": "API rate limit exceeded."
                    },
                    status_code=429
                ),
                # Return a 200 on the second attempt
                MockApiResponse(
                    json_data={
                        "access_token": "mock_access_token",
                        "refresh_token": "mock_refresh_token",
                        "expires_in": 60
                    },
                    status_code=200
                ),
            ]

            # Ensure that we were able to get the token, if not retrying this would be impossible
            self.assertEqual(f"{refreshing_token}", "mock_access_token")
            self.assertEqual(identity_mock.call_count, 2)

    def test_retries_on_429_status_code_using_refresh_token(self):
        """
        Ensures that in the event of a 429 HTTP Status Code being returned when communicating with an identity
        provider, the request is retried.
        """
        refreshing_token = RefreshingToken(api_configuration=self.config)

        with patch("requests.post") as identity_mock:

            identity_mock.side_effect=[
                # Get initial access token
                MockApiResponse(
                    json_data={
                        "access_token": "mock_access_token",
                        "refresh_token": "mock_refresh_token",
                        "expires_in": 1  # Expires almost immediately
                    },
                    status_code=200
                ),
                # Return a 429 on the second attempt
                MockApiResponse(
                    json_data={
                        "error": "rate_limit",
                        "error_description": "API rate limit exceeded."
                    },
                    status_code=429
                ),
                # Return a 200 on the third attempt
                MockApiResponse(
                    json_data={
                        "access_token": "mock_access_token_2",
                        "refresh_token": "mock_refresh_token",
                        "expires_in": 60
                    },
                    status_code=200
                ),
            ]

            # Ensure that we were able to get the first access token
            self.assertEqual(f"{refreshing_token}", "mock_access_token")

            sleep(1)  # Wait for initial token to expire

            # Try and get access token again forcing refresh, if we can get it then retry was called
            self.assertEqual(f"{refreshing_token}", "mock_access_token_2")
            self.assertEqual(identity_mock.call_count, 3)

    def test_does_not_retry_on_4xx_status_code_other_than_429(self):
        """
        Ensures that we do not retry on other common 4xx status codes such as 400 - Bad Request
        """
        refreshing_token = RefreshingToken(api_configuration=self.config)

        with patch("requests.post") as identity_mock:
            identity_mock.side_effect = [
                # Return a 400
                MockApiResponse(
                    json_data={
                        "error": "invalid_grant",
                        "error_description": "The refresh token is invalid or expired."
                    },
                    status_code=400
                ),
            ]

            # Ensure that a 400 is raised as an error and not retried
            with self.assertRaises(ValueError) as bad_request_exception:
                self.force_refresh(refreshing_token)

            self.assertEqual(identity_mock.call_count, 1)  # No retrying
            self.assertIn("invalid_grant", str(bad_request_exception.exception))

    def test_retries_on_429s_up_till_retry_limit(self):
        """
        Ensures that the refreshing token only retries up until the retry limit to prevent
        an infinite retry loop
        """
        refreshing_token = RefreshingToken(api_configuration=self.config)

        refreshing_token.retry_limit = 2  # Override default to ensure test runs in reasonable amount of time
        expected_requests = 1 + refreshing_token.retry_limit  # Initial request plus expected number retries

        with patch("requests.post") as identity_mock:
            identity_mock.side_effect = [
                MockApiResponse(
                    json_data={
                        "error": "rate_limit",
                        "error_description": "API rate limit exceeded."
                    },
                    status_code=429,
                    headers={}
                )
            ] * expected_requests  # Return a 429 every time up until expected number of attempts

            # Ensure that a an error is raised once reaching the retry limit
            with self.assertRaises(ValueError) as retry_limit_error:
                self.force_refresh(refreshing_token)

            self.assertIn("Max retry limit", str(retry_limit_error.exception))

            # Ensure that we only tried as many times as expected
            self.assertEqual(expected_requests, identity_mock.call_count)

    @parameterized.expand([
        ["One Attempt", 1, 2],
        ["Two Attempts", 2, 2 + 4],
        ["Three Attempts", 3, 2 + 4 + 8],
        ["Four Attempts", 4, 2 + 4 + 8 + 16],
    ])
    def test_retries_on_429s_uses_exponential_back_off_if_no_retry_after_header(self, _, number_attempts_till_success,
                                                                                expected_delay):
        """
        Ensures that if no "Retry-After" header is provided then a simple exponential back-off strategy is used. This
        is confirmed by checking that the time taken to successfully retrieve a token scales exponentially as the number
        of retries increases.
        """
        refreshing_token = RefreshingToken(api_configuration=self.config)
        refreshing_token.backoff_base = 2  # Use a 2 second base for calculating back-off

        with patch("requests.post", side_effect=[
            # Return a 429 on the first attempts
            MockApiResponse(
                json_data={
                    "error": "rate_limit",
                    "error_description": "API rate limit exceeded."
                },
                status_code=429,
            )] * number_attempts_till_success +
            # Return a 200 on the last attempt
            [
                MockApiResponse(
                    json_data={
                        "access_token": "mock_access_token",
                        "refresh_token": "mock_refresh_token",
                        "expires_in": 60
                    },
                    status_code=200
                )
            ]
        ):
            start = time()
            # Ensure that we were able to get the token, if not retrying this would be impossible
            self.assertEqual(f"{refreshing_token}", "mock_access_token")
            elapsed = time() - start
            # Ensure that the elapsed time is as expected
            self.assertEqual(int(elapsed), expected_delay)

    @parameterized.expand([
        ["Zero", 0],
        ["Positive Int", 5],
        ["Positive Int2", 8]
        # Not possible to have a negative integer returned in this header
    ])
    def test_retries_on_429s_uses_retry_after_header_with_seconds_delay_if_exists(self, _, seconds_delay):
        """
        Ensures that if a seconds delay is contained in the "Retry-After" header then a retry is attempted after
        the appropriate amount of time.

        :param _: The name of the tests
        :param seconds_delay: The number of seconds to wait before retrying
        """
        refreshing_token = RefreshingToken(api_configuration=self.config)

        with patch("requests.post", side_effect=[
            # Return a 429 on the first attempt
            MockApiResponse(
                json_data={
                    "error": "rate_limit",
                    "error_description": "API rate limit exceeded."
                },
                status_code=429,
                headers={"Retry-After": str(seconds_delay)}
            ),
            # Return a 200 on the second attempt
            MockApiResponse(
                json_data={
                    "access_token": "mock_access_token",
                    "refresh_token": "mock_refresh_token",
                    "expires_in": 60
                },
                status_code=200
            ),
        ]):
            start = time()
            # Ensure that we were able to get the token, if not retrying this would be impossible
            self.assertEqual(f"{refreshing_token}", "mock_access_token")
            elapsed = time() - start
            # Ensure that the wait was for an appropriate amount of time
            self.assertEqual(int(elapsed), seconds_delay)

    def test_retries_on_429s_uses_retry_after_header_with_http_date_in_future_if_exists(self):
        """
        Ensures that if the HTTP Date returned on the "Retry-After" header is x seconds in the future
        it takes approximately x seconds to retry and get the token.
        """
        time_to_wait = 5

        refreshing_token = RefreshingToken(api_configuration=self.config)

        with patch("requests.post", side_effect=[
            # Return a 429 on the first attempt
            MockApiResponse(
                json_data={
                    "error": "rate_limit",
                    "error_description": "API rate limit exceeded."
                },
                status_code=429,
                headers={"Retry-After": self.convert_to_http_date(datetime.utcnow() + timedelta(seconds=time_to_wait))}
            ),
            # Return a 200 on the second attempt
            MockApiResponse(
                json_data={
                    "access_token": "mock_access_token",
                    "refresh_token": "mock_refresh_token",
                    "expires_in": 60
                },
                status_code=200
            ),
        ]):
            start = time()
            # Ensure that we were able to get the token, if not retrying this would be impossible
            self.assertEqual(f"{refreshing_token}", "mock_access_token")
            elapsed = time() - start
            # Ensure that the wait was for an appropriate amount of time, because the seconds to wait are calculated
            # here instead of being provided directly the delay could be a second less
            self.assertGreaterEqual(int(elapsed), time_to_wait - 1)
            self.assertLessEqual(int(elapsed), time_to_wait)

    def test_retries_on_429s_uses_retry_after_header_with_http_date_in_past_if_exists(self):
        """
        Ensures that if the HTTP Date returned on the "Retry-After" header is x seconds in the past
        an retry attempt to get the token is made immediately
        """
        refreshing_token = RefreshingToken(api_configuration=self.config)

        with patch("requests.post", side_effect=[
            # Return a 429 on the first attempt
            MockApiResponse(
                json_data={
                    "error": "rate_limit",
                    "error_description": "API rate limit exceeded."
                },
                status_code=429,
                headers={"Retry-After": self.convert_to_http_date(datetime.utcnow() - timedelta(seconds=5))}
            ),
            # Return a 200 on the second attempt
            MockApiResponse(
                json_data={
                    "access_token": "mock_access_token",
                    "refresh_token": "mock_refresh_token",
                    "expires_in": 60
                },
                status_code=200
            ),
        ]):
            start = time()
            # Ensure that we were able to get the token, if not retrying this would be impossible
            self.assertEqual(f"{refreshing_token}", "mock_access_token")
            elapsed = time() - start
            # Ensure that the wait was essentially no wait before retrying
            self.assertLess(elapsed, 1)

    def test_can_use_id_provider_handler_to_provide_retry_after_header_from_custom_header(self):
        """
        Ensures that the "Retry-After" header can be used after being created from a custom header using the
        id_provider_response_handler.
        """

        time_to_wait = 5

        def header_creator(id_provider_response):

            rate_limit_reset = id_provider_response.headers.get("X-Rate-Limit-Reset", None)

            if rate_limit_reset is not None:
                id_provider_response.headers["Retry-After"] = max(int(rate_limit_reset - datetime.utcnow().timestamp()), 0)

        refreshing_token = RefreshingToken(api_configuration=self.config, id_provider_response_handler=header_creator)

        with patch("requests.post", side_effect=[
            # Return a 429 on the first attempt
            MockApiResponse(
                json_data={
                    "error": "rate_limit",
                    "error_description": "API rate limit exceeded."
                },
                status_code=429,
                headers={"X-Rate-Limit-Reset": datetime.utcnow().timestamp() + time_to_wait}
            ),
            # Return a 200 on the second attempt
            MockApiResponse(
                json_data={
                    "access_token": "mock_access_token",
                    "refresh_token": "mock_refresh_token",
                    "expires_in": 60
                },
                status_code=200
            ),
        ]):
            start = time()
            # Ensure that we were able to get the token, if not retrying this would be impossible
            self.assertEqual(f"{refreshing_token}", "mock_access_token")
            elapsed = time() - start
            # Ensure that the wait was for an appropriate amount of time, because the seconds to wait are calculated
            # here instead of being provided directly the delay could be a second less
            self.assertGreaterEqual(int(elapsed), time_to_wait-1)
            self.assertLessEqual(int(elapsed), time_to_wait)

    @unittest.skip("Not valid test when using Okta caching proxy")
    def test_retries_against_id_provider_after_hitting_rate_limit(self):
        """
        Integration tests which calls the identity provider specified in the provided credentials (Okta in the
        CI pipeline) and asserts that when the rate limit is hit a retry is made and the access token can be
        successfully retrieved without throwing.
        """
        responses = []

        def record_response(id_provider_response):
            nonlocal responses
            responses.append(id_provider_response.status_code)

        # Create 5 independent tokens
        refreshing_token1 = RefreshingToken(api_configuration=self.config, id_provider_response_handler=record_response)
        refreshing_token2 = RefreshingToken(api_configuration=self.config, id_provider_response_handler=record_response)
        refreshing_token3 = RefreshingToken(api_configuration=self.config, id_provider_response_handler=record_response)
        refreshing_token4 = RefreshingToken(api_configuration=self.config, id_provider_response_handler=record_response)
        refreshing_token5 = RefreshingToken(api_configuration=self.config, id_provider_response_handler=record_response)

        # Get the access token from each one on an independent thread
        thread1 = Thread(target=self.force_refresh, args=[refreshing_token1])
        thread2 = Thread(target=self.force_refresh, args=[refreshing_token2])
        thread3 = Thread(target=self.force_refresh, args=[refreshing_token3])
        thread4 = Thread(target=self.force_refresh, args=[refreshing_token4])
        thread5 = Thread(target=self.force_refresh, args=[refreshing_token5])

        # Run all threads
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()

        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()

        # Count the status codes returned
        result = dict((i, responses.count(i)) for i in responses)

        # Expect to see at least a single 429
        self.assertGreaterEqual(result[429], 1)
        # And 5 200s eventually
        self.assertEqual(result[200], 5)

    def test_get_access_token_with_special_chars_in_credentials(self):
        # create the problematic credentials
        config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())
        config.password = "abcd:efg"
        refreshing_token = RefreshingToken(api_configuration=config)

        with patch("requests.post") as identity_mock:
            identity_mock.side_effect = [
                MockApiResponse(
                    json_data={
                        "access_token": "mock_access_token",
                        "refresh_token": "mock_refresh_token",
                        "expires_in": 60
                    },
                    status_code=200
                )]
            # Ensure that we were able to get the token
            self.assertEqual(f"{refreshing_token}", "mock_access_token")

    def test_get_access_token_with_path_chars_in_credentials(self):
        # create the problematic credentials
        config = ApiConfigurationLoader.load(CredentialsSource.secrets_path())
        config.password = "some/random/url?key=value"
        config.username = "test"
        config.client_id = "test"
        config.client_secret = "test"
        refreshing_token = RefreshingToken(api_configuration=config)
        with patch("requests.post") as identity_mock:
            identity_mock.side_effect = [
                MockApiResponse(
                    json_data={
                        "access_token": "mock_access_token",
                        "refresh_token": "mock_refresh_token",
                        "expires_in": 60
                    },
                    status_code=200
                )]
            self.assertEqual(f"{refreshing_token}", "mock_access_token")
            expected_password_encoding = "some%2Frandom%2Furl%3Fkey%3Dvalue"
            expected_request_body = f"grant_type=password&username=test" \
                                    f"&password={expected_password_encoding}&scope=openid client groups offline_access" \
                                    f"&client_id=test&client_secret=test"
            self.assertEqual(identity_mock.call_args[1]["data"], expected_request_body)
