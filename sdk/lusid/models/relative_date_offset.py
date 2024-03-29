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


from typing import Any, Dict
from pydantic import BaseModel, Field, StrictInt, constr

class RelativeDateOffset(BaseModel):
    """
    Defines a date offset which is relative to some anchor date.  # noqa: E501
    """
    days: StrictInt = Field(..., description="The number of business days to add to the anchor date.")
    business_day_convention: constr(strict=True, min_length=1) = Field(..., alias="businessDayConvention", description="The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.    Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].")
    __properties = ["days", "businessDayConvention"]

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
    def from_json(cls, json_str: str) -> RelativeDateOffset:
        """Create an instance of RelativeDateOffset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RelativeDateOffset:
        """Create an instance of RelativeDateOffset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RelativeDateOffset.parse_obj(obj)

        _obj = RelativeDateOffset.parse_obj({
            "days": obj.get("days"),
            "business_day_convention": obj.get("businessDayConvention")
        })
        return _obj
