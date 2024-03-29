# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class DeleteModes(str, Enum):
    """
    DeleteModes
    """

    """
    allowed enum values
    """
    SOFT = 'soft'
    HARD = 'hard'

    @classmethod
    def from_json(cls, json_str: str) -> DeleteModes:
        """Create an instance of DeleteModes from a JSON string"""
        return DeleteModes(json.loads(json_str))
