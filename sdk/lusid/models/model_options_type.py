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





class ModelOptionsType(str, Enum):
    """
    ModelOptionsType
    """

    """
    allowed enum values
    """
    INVALID = 'Invalid'
    OPAQUEMODELOPTIONS = 'OpaqueModelOptions'
    EMPTYMODELOPTIONS = 'EmptyModelOptions'
    INDEXMODELOPTIONS = 'IndexModelOptions'
    FXFORWARDMODELOPTIONS = 'FxForwardModelOptions'
    FUNDINGLEGMODELOPTIONS = 'FundingLegModelOptions'
    EQUITYMODELOPTIONS = 'EquityModelOptions'
    CDSMODELOPTIONS = 'CdsModelOptions'

    @classmethod
    def from_json(cls, json_str: str) -> ModelOptionsType:
        """Create an instance of ModelOptionsType from a JSON string"""
        return ModelOptionsType(json.loads(json_str))
