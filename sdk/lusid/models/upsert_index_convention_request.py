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
from pydantic.v1 import StrictStr, Field, BaseModel, Field 
from lusid.models.index_convention import IndexConvention

class UpsertIndexConventionRequest(BaseModel):
    """
    Index convention that is to be stored in the convention data store.  Only one of these must be present.  # noqa: E501
    """
    index_convention: Optional[IndexConvention] = Field(None, alias="indexConvention")
    __properties = ["indexConvention"]

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
    def from_json(cls, json_str: str) -> UpsertIndexConventionRequest:
        """Create an instance of UpsertIndexConventionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of index_convention
        if self.index_convention:
            _dict['indexConvention'] = self.index_convention.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpsertIndexConventionRequest:
        """Create an instance of UpsertIndexConventionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpsertIndexConventionRequest.parse_obj(obj)

        _obj = UpsertIndexConventionRequest.parse_obj({
            "index_convention": IndexConvention.from_dict(obj.get("indexConvention")) if obj.get("indexConvention") is not None else None
        })
        return _obj
