# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

class TransactionTypeDetails(BaseModel):
    """
    TransactionTypeDetails
    """
    scope: Optional[StrictStr] = Field(None, description="The scope in which the TransactionType was resolved. If the portfolio has a TransactionTypeScope, this will have been used. Otherwise the default scope will have been used.")
    source: Optional[StrictStr] = Field(None, description="The source in which the TransactionType was resolved.")
    type: Optional[StrictStr] = Field(None, description="The resolved TransactionType. More information on TransactionType resolution can be found at https://support.lusid.com/docs/how-does-lusid-resolve-transactions-to-transaction-types")
    __properties = ["scope", "source", "type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TransactionTypeDetails:
        """Create an instance of TransactionTypeDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if source (nullable) is None
        # and __fields_set__ contains the field
        if self.source is None and "source" in self.__fields_set__:
            _dict['source'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionTypeDetails:
        """Create an instance of TransactionTypeDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionTypeDetails.parse_obj(obj)

        _obj = TransactionTypeDetails.parse_obj({
            "scope": obj.get("scope"),
            "source": obj.get("source"),
            "type": obj.get("type")
        })
        return _obj