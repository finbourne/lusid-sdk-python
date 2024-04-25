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
from pydantic.v1 import BaseModel, Field, conlist, constr
from lusid.models.staging_rule import StagingRule

class UpdateStagingRuleSetRequest(BaseModel):
    """
    UpdateStagingRuleSetRequest
    """
    display_name: Optional[constr(strict=True, max_length=256, min_length=1)] = Field(None, alias="displayName", description="The name of the staging rule set.")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="A description for the staging rule set.")
    rules: conlist(StagingRule) = Field(..., description="The list of staging rules that apply to a specific entity type.")
    __properties = ["displayName", "description", "rules"]

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
    def from_json(cls, json_str: str) -> UpdateStagingRuleSetRequest:
        """Create an instance of UpdateStagingRuleSetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateStagingRuleSetRequest:
        """Create an instance of UpdateStagingRuleSetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateStagingRuleSetRequest.parse_obj(obj)

        _obj = UpdateStagingRuleSetRequest.parse_obj({
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "rules": [StagingRule.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None
        })
        return _obj