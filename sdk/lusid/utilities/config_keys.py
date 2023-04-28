from pathlib import Path
import json


class ConfigKeys:
    config_key_path = "config_keys.json"

    @classmethod
    def get(cls):
        with open(Path(__file__).parent.joinpath(cls.config_key_path)) as json_file:
            config_keys = json.load(json_file)

        return config_keys
