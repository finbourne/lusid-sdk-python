import unittest

from parameterized import parameterized

from lusid import ApiConfiguration


class ApiConfigurationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_okta_url_regex = '^http(s)?:\/\/.*\.okta\.com\/oauth2\/.*\/v\d+\/token$'

    @parameterized.expand([
        # Okta urls without proper suffix
        'https://lusid-testdomain.okta.com/oauth2/sdf7a6sd8f76asd976f/',
        'https://lusid-testdomain.okta.com/oauth2/sdf7a6sd8f76asd976f',
        # Okta urls with proper suffix
        'https://lusid-testdomain.okta.com/oauth2/sdf7a6sd8f76asd976f/v1/token',
        'https://lusid-testdomain.okta.com/oauth2/sdf7a6sd8f76asd976f/v1/token/',
        'https://lusid-testdomain.okta.com/oauth2/sdf7a6sd8f76asd976f/v2/token',
        'https://lusid-testdomain.okta.com/oauth2/sdf7a6sd8f76asd976f/v2/token/',
        # 2 digit version
        'https://lusid-testdomain.okta.com/oauth2/sdf7a6sd8f76asd976f/v10/token',
        'https://lusid-testdomain.okta.com/oauth2/sdf7a6sd8f76asd976f/v10/token/'
    ])
    def test_okta_token_url_without_proper_suffix(self, token_url):
        api_config = ApiConfiguration(token_url=token_url)
        self.assertRegex(api_config.token_url, self.valid_okta_url_regex)

    @parameterized.expand([
        # Non okta urls with a token suffix
        'https://foo.bar.com/oauth2/asd34fhas34dufhasdf/v1/token',
        'https://foo.bar.com/oauth2/asdfh756asdufhasdf/v1/token/',
        # Non okta urls without a token suffix
        'https://foo.bar.com/oauth2/asd34fhas34dufhasdf',
        'https://foo.bar.com/oauth2/asdfh756asdufhasdf/'
    ])
    def test_non_okta_token_url_with_proper_suffix(self, token_url):
        api_config = ApiConfiguration(token_url=token_url)
        self.assertEqual(api_config.token_url, token_url)
