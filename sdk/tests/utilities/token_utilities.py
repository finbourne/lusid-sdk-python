from lusid import ApiClientBuilder


class TokenUtilities:

    @staticmethod
    def get_okta_tokens(secrets_path):
        original_token = ""
        refresh_token = ""

        def extract_refresh_token(okta_response):
            nonlocal refresh_token
            nonlocal original_token
            okta_json = okta_response.json()
            refresh_token = okta_json["refresh_token"]
            original_token = okta_json["access_token"]

        client = ApiClientBuilder().build(secrets_path, extract_refresh_token)
        repr(client.configuration.access_token)

        return original_token, refresh_token
