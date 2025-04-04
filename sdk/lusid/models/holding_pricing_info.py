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


from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist 
from lusid.models.specific_holding_pricing_info import SpecificHoldingPricingInfo

class HoldingPricingInfo(BaseModel):
    """
    Enables price quotes to be created from Holding fields as either overrides or fallbacks to the Market Data  resolution process. For example, we may wish to price an instrument at Cost if Market Data resolution fails.  We may also wish to always price Bonds using the LastTradedPrice on the corresponding Holding.  # noqa: E501
    """
    fallback_field:  Optional[StrictStr] = Field(None,alias="fallbackField", description="The default Holding field to fall back on if the Market Data resolution process fails to find a price quote.") 
    override_field:  Optional[StrictStr] = Field(None,alias="overrideField", description="The default Holding field to be used as an override for instrument price quotes. This cannot be specified  along with a FallbackField or any SpecificFallbacks, since we'll never attempt Market Data resolution  for price quotes if this field is populated.") 
    specific_fallbacks: Optional[conlist(SpecificHoldingPricingInfo)] = Field(None, alias="specificFallbacks", description="Allows a user to specify fallbacks using Holding fields for sources that match a particular DependencySourceFilter.")
    specific_overrides: Optional[conlist(SpecificHoldingPricingInfo)] = Field(None, alias="specificOverrides", description="Allows a user to specify overrides using Holding fields for sources that match a particular DependencySourceFilter.")
    __properties = ["fallbackField", "overrideField", "specificFallbacks", "specificOverrides"]

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
    def from_json(cls, json_str: str) -> HoldingPricingInfo:
        """Create an instance of HoldingPricingInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in specific_fallbacks (list)
        _items = []
        if self.specific_fallbacks:
            for _item in self.specific_fallbacks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specificFallbacks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in specific_overrides (list)
        _items = []
        if self.specific_overrides:
            for _item in self.specific_overrides:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specificOverrides'] = _items
        # set to None if fallback_field (nullable) is None
        # and __fields_set__ contains the field
        if self.fallback_field is None and "fallback_field" in self.__fields_set__:
            _dict['fallbackField'] = None

        # set to None if override_field (nullable) is None
        # and __fields_set__ contains the field
        if self.override_field is None and "override_field" in self.__fields_set__:
            _dict['overrideField'] = None

        # set to None if specific_fallbacks (nullable) is None
        # and __fields_set__ contains the field
        if self.specific_fallbacks is None and "specific_fallbacks" in self.__fields_set__:
            _dict['specificFallbacks'] = None

        # set to None if specific_overrides (nullable) is None
        # and __fields_set__ contains the field
        if self.specific_overrides is None and "specific_overrides" in self.__fields_set__:
            _dict['specificOverrides'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HoldingPricingInfo:
        """Create an instance of HoldingPricingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HoldingPricingInfo.parse_obj(obj)

        _obj = HoldingPricingInfo.parse_obj({
            "fallback_field": obj.get("fallbackField"),
            "override_field": obj.get("overrideField"),
            "specific_fallbacks": [SpecificHoldingPricingInfo.from_dict(_item) for _item in obj.get("specificFallbacks")] if obj.get("specificFallbacks") is not None else None,
            "specific_overrides": [SpecificHoldingPricingInfo.from_dict(_item) for _item in obj.get("specificOverrides")] if obj.get("specificOverrides") is not None else None
        })
        return _obj
