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
from pydantic.v1 import StrictStr, Field, BaseModel, Field 
from lusid.models.amount import Amount
from lusid.models.share_class_amount import ShareClassAmount

class ShareClassDealingBreakdown(BaseModel):
    """
    The breakdown of Dealing for a Share Class.  # noqa: E501
    """
    class_dealing: Dict[str, ShareClassAmount] = Field(..., alias="classDealing", description="Bucket of detail for any 'Dealing' specific to the share class that has occured inside the queried period.")
    class_dealing_units: Dict[str, Amount] = Field(..., alias="classDealingUnits", description="Bucket of detail for any 'Dealing' units specific to the share class that has occured inside the queried period.")
    __properties = ["classDealing", "classDealingUnits"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ShareClassDealingBreakdown:
        """Create an instance of ShareClassDealingBreakdown from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in class_dealing (dict)
        _field_dict = {}
        if self.class_dealing:
            for _key in self.class_dealing:
                if self.class_dealing[_key]:
                    _field_dict[_key] = self.class_dealing[_key].to_dict()
            _dict['classDealing'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in class_dealing_units (dict)
        _field_dict = {}
        if self.class_dealing_units:
            for _key in self.class_dealing_units:
                if self.class_dealing_units[_key]:
                    _field_dict[_key] = self.class_dealing_units[_key].to_dict()
            _dict['classDealingUnits'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ShareClassDealingBreakdown:
        """Create an instance of ShareClassDealingBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ShareClassDealingBreakdown.parse_obj(obj)

        _obj = ShareClassDealingBreakdown.parse_obj({
            "class_dealing": dict(
                (_k, ShareClassAmount.from_dict(_v))
                for _k, _v in obj.get("classDealing").items()
            )
            if obj.get("classDealing") is not None
            else None,
            "class_dealing_units": dict(
                (_k, Amount.from_dict(_v))
                for _k, _v in obj.get("classDealingUnits").items()
            )
            if obj.get("classDealingUnits") is not None
            else None
        })
        return _obj
