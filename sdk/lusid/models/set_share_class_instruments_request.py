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


from typing import Any, Dict, List
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist 
from lusid.models.instrument_resolution_detail import InstrumentResolutionDetail

class SetShareClassInstrumentsRequest(BaseModel):
    """
    The request used to create a Fund.  # noqa: E501
    """
    share_class_instrument_scopes: conlist(StrictStr) = Field(..., alias="shareClassInstrumentScopes", description="The scopes in which the instruments lie, currently limited to one.")
    share_class_instruments: conlist(InstrumentResolutionDetail) = Field(..., alias="shareClassInstruments", description="Details the user-provided instrument identifiers and the instrument resolved from them.")
    __properties = ["shareClassInstrumentScopes", "shareClassInstruments"]

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
    def from_json(cls, json_str: str) -> SetShareClassInstrumentsRequest:
        """Create an instance of SetShareClassInstrumentsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in share_class_instruments (list)
        _items = []
        if self.share_class_instruments:
            for _item in self.share_class_instruments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shareClassInstruments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetShareClassInstrumentsRequest:
        """Create an instance of SetShareClassInstrumentsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetShareClassInstrumentsRequest.parse_obj(obj)

        _obj = SetShareClassInstrumentsRequest.parse_obj({
            "share_class_instrument_scopes": obj.get("shareClassInstrumentScopes"),
            "share_class_instruments": [InstrumentResolutionDetail.from_dict(_item) for _item in obj.get("shareClassInstruments")] if obj.get("shareClassInstruments") is not None else None
        })
        return _obj
