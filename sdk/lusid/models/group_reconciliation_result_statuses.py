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
from pydantic.v1 import BaseModel, Field, StrictInt
from lusid.models.link import Link

class GroupReconciliationResultStatuses(BaseModel):
    """
    GroupReconciliationResultStatuses
    """
    count_new: StrictInt = Field(..., alias="countNew", description="The number of comparison results of resultStatus \"New\" with this instanceId and reconciliationType")
    link_new: Link = Field(..., alias="linkNew")
    count_confirmed: StrictInt = Field(..., alias="countConfirmed", description="The number of comparison results of resultStatus \"Confirmed\" with this instanceId and reconciliationType")
    link_confirmed: Link = Field(..., alias="linkConfirmed")
    count_changed: StrictInt = Field(..., alias="countChanged", description="The number of comparison results of resultStatus \"Changed\" with this instanceId and reconciliationType")
    link_changed: Link = Field(..., alias="linkChanged")
    __properties = ["countNew", "linkNew", "countConfirmed", "linkConfirmed", "countChanged", "linkChanged"]

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
    def from_json(cls, json_str: str) -> GroupReconciliationResultStatuses:
        """Create an instance of GroupReconciliationResultStatuses from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of link_new
        if self.link_new:
            _dict['linkNew'] = self.link_new.to_dict()
        # override the default output from pydantic by calling `to_dict()` of link_confirmed
        if self.link_confirmed:
            _dict['linkConfirmed'] = self.link_confirmed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of link_changed
        if self.link_changed:
            _dict['linkChanged'] = self.link_changed.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupReconciliationResultStatuses:
        """Create an instance of GroupReconciliationResultStatuses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupReconciliationResultStatuses.parse_obj(obj)

        _obj = GroupReconciliationResultStatuses.parse_obj({
            "count_new": obj.get("countNew"),
            "link_new": Link.from_dict(obj.get("linkNew")) if obj.get("linkNew") is not None else None,
            "count_confirmed": obj.get("countConfirmed"),
            "link_confirmed": Link.from_dict(obj.get("linkConfirmed")) if obj.get("linkConfirmed") is not None else None,
            "count_changed": obj.get("countChanged"),
            "link_changed": Link.from_dict(obj.get("linkChanged")) if obj.get("linkChanged") is not None else None
        })
        return _obj