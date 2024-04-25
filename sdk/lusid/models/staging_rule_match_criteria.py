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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

class StagingRuleMatchCriteria(BaseModel):
    """
    StagingRuleMatchCriteria
    """
    action_in: Optional[conlist(StrictStr)] = Field(None, alias="actionIn")
    requesting_user: Optional[constr(strict=True, max_length=16384, min_length=0)] = Field(None, alias="requestingUser")
    entity_attributes: Optional[constr(strict=True, max_length=16384, min_length=0)] = Field(None, alias="entityAttributes")
    changed_attribute_name_in: Optional[conlist(StrictStr)] = Field(None, alias="changedAttributeNameIn")
    __properties = ["actionIn", "requestingUser", "entityAttributes", "changedAttributeNameIn"]

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
    def from_json(cls, json_str: str) -> StagingRuleMatchCriteria:
        """Create an instance of StagingRuleMatchCriteria from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if action_in (nullable) is None
        # and __fields_set__ contains the field
        if self.action_in is None and "action_in" in self.__fields_set__:
            _dict['actionIn'] = None

        # set to None if requesting_user (nullable) is None
        # and __fields_set__ contains the field
        if self.requesting_user is None and "requesting_user" in self.__fields_set__:
            _dict['requestingUser'] = None

        # set to None if entity_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.entity_attributes is None and "entity_attributes" in self.__fields_set__:
            _dict['entityAttributes'] = None

        # set to None if changed_attribute_name_in (nullable) is None
        # and __fields_set__ contains the field
        if self.changed_attribute_name_in is None and "changed_attribute_name_in" in self.__fields_set__:
            _dict['changedAttributeNameIn'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StagingRuleMatchCriteria:
        """Create an instance of StagingRuleMatchCriteria from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StagingRuleMatchCriteria.parse_obj(obj)

        _obj = StagingRuleMatchCriteria.parse_obj({
            "action_in": obj.get("actionIn"),
            "requesting_user": obj.get("requestingUser"),
            "entity_attributes": obj.get("entityAttributes"),
            "changed_attribute_name_in": obj.get("changedAttributeNameIn")
        })
        return _obj