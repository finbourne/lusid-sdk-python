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
from pydantic import BaseModel, Field, StrictBool, constr, validator

class SetTransactionConfigurationAlias(BaseModel):
    """
    SetTransactionConfigurationAlias
    """
    type: constr(strict=True, max_length=64, min_length=1) = Field(...)
    description: constr(strict=True, max_length=1024, min_length=0) = Field(...)
    transaction_class: constr(strict=True, min_length=1) = Field(..., alias="transactionClass")
    transaction_role: constr(strict=True, min_length=1) = Field(..., alias="transactionRole")
    is_default: Optional[StrictBool] = Field(None, alias="isDefault")
    __properties = ["type", "description", "transactionClass", "transactionRole", "isDefault"]

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

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
    def from_json(cls, json_str: str) -> SetTransactionConfigurationAlias:
        """Create an instance of SetTransactionConfigurationAlias from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetTransactionConfigurationAlias:
        """Create an instance of SetTransactionConfigurationAlias from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetTransactionConfigurationAlias.parse_obj(obj)

        _obj = SetTransactionConfigurationAlias.parse_obj({
            "type": obj.get("type"),
            "description": obj.get("description"),
            "transaction_class": obj.get("transactionClass"),
            "transaction_role": obj.get("transactionRole"),
            "is_default": obj.get("isDefault")
        })
        return _obj