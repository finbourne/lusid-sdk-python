from pathlib import Path


class CredentialsSource:

    @classmethod
    def secrets_path(cls) -> Path:
        return Path(__file__).parent.parent.joinpath('secrets.json')
