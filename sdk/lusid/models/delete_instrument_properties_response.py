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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist 
from lusid.models.link import Link
from lusid.models.staged_modifications_info import StagedModificationsInfo

class DeleteInstrumentPropertiesResponse(BaseModel):
    """
    DeleteInstrumentPropertiesResponse
    """
    as_at: datetime = Field(..., alias="asAt", description="The as-at datetime at which properties were deleted.")
    staged_modifications: Optional[StagedModificationsInfo] = Field(None, alias="stagedModifications")
    links: Optional[conlist(Link)] = None
    __properties = ["asAt", "stagedModifications", "links"]

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
    def from_json(cls, json_str: str) -> DeleteInstrumentPropertiesResponse:
        """Create an instance of DeleteInstrumentPropertiesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of staged_modifications
        if self.staged_modifications:
            _dict['stagedModifications'] = self.staged_modifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeleteInstrumentPropertiesResponse:
        """Create an instance of DeleteInstrumentPropertiesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeleteInstrumentPropertiesResponse.parse_obj(obj)

        _obj = DeleteInstrumentPropertiesResponse.parse_obj({
            "as_at": obj.get("asAt"),
            "staged_modifications": StagedModificationsInfo.from_dict(obj.get("stagedModifications")) if obj.get("stagedModifications") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
