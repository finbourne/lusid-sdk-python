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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictInt 
from lusid.models.link import Link

class GroupReconciliationResultTypes(BaseModel):
    """
    GroupReconciliationResultTypes
    """
    count_match: StrictInt = Field(..., alias="countMatch", description="The number of comparison results of resultType \"Match\" with this instanceId and reconciliationType")
    link_matches: Link = Field(..., alias="linkMatches")
    count_partial_match: StrictInt = Field(..., alias="countPartialMatch", description="The number of comparison results of resultType \"PartialMatch\" with this instanceId and reconciliationType")
    link_partial_matches: Link = Field(..., alias="linkPartialMatches")
    count_break: StrictInt = Field(..., alias="countBreak", description="The number of comparison results of resultType \"Break\" with this instanceId and reconciliationType")
    link_breaks: Link = Field(..., alias="linkBreaks")
    count_resolved: StrictInt = Field(..., alias="countResolved", description="The number of comparison results of resultType \"Resolved\" with this instanceId and reconciliationType")
    link_resolved: Link = Field(..., alias="linkResolved")
    __properties = ["countMatch", "linkMatches", "countPartialMatch", "linkPartialMatches", "countBreak", "linkBreaks", "countResolved", "linkResolved"]

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
    def from_json(cls, json_str: str) -> GroupReconciliationResultTypes:
        """Create an instance of GroupReconciliationResultTypes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of link_matches
        if self.link_matches:
            _dict['linkMatches'] = self.link_matches.to_dict()
        # override the default output from pydantic by calling `to_dict()` of link_partial_matches
        if self.link_partial_matches:
            _dict['linkPartialMatches'] = self.link_partial_matches.to_dict()
        # override the default output from pydantic by calling `to_dict()` of link_breaks
        if self.link_breaks:
            _dict['linkBreaks'] = self.link_breaks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of link_resolved
        if self.link_resolved:
            _dict['linkResolved'] = self.link_resolved.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupReconciliationResultTypes:
        """Create an instance of GroupReconciliationResultTypes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupReconciliationResultTypes.parse_obj(obj)

        _obj = GroupReconciliationResultTypes.parse_obj({
            "count_match": obj.get("countMatch"),
            "link_matches": Link.from_dict(obj.get("linkMatches")) if obj.get("linkMatches") is not None else None,
            "count_partial_match": obj.get("countPartialMatch"),
            "link_partial_matches": Link.from_dict(obj.get("linkPartialMatches")) if obj.get("linkPartialMatches") is not None else None,
            "count_break": obj.get("countBreak"),
            "link_breaks": Link.from_dict(obj.get("linkBreaks")) if obj.get("linkBreaks") is not None else None,
            "count_resolved": obj.get("countResolved"),
            "link_resolved": Link.from_dict(obj.get("linkResolved")) if obj.get("linkResolved") is not None else None
        })
        return _obj
