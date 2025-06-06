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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist, constr, validator 
from lusid.models.compliance_step import ComplianceStep

class ComplianceTemplateVariationDto(BaseModel):
    """
    ComplianceTemplateVariationDto
    """
    label:  StrictStr = Field(...,alias="label") 
    description:  StrictStr = Field(...,alias="description") 
    outcome_description:  Optional[StrictStr] = Field(None,alias="outcomeDescription") 
    referenced_group_label:  Optional[StrictStr] = Field(None,alias="referencedGroupLabel") 
    steps: conlist(ComplianceStep) = Field(...)
    __properties = ["label", "description", "outcomeDescription", "referencedGroupLabel", "steps"]

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
    def from_json(cls, json_str: str) -> ComplianceTemplateVariationDto:
        """Create an instance of ComplianceTemplateVariationDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item in self.steps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['steps'] = _items
        # set to None if outcome_description (nullable) is None
        # and __fields_set__ contains the field
        if self.outcome_description is None and "outcome_description" in self.__fields_set__:
            _dict['outcomeDescription'] = None

        # set to None if referenced_group_label (nullable) is None
        # and __fields_set__ contains the field
        if self.referenced_group_label is None and "referenced_group_label" in self.__fields_set__:
            _dict['referencedGroupLabel'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceTemplateVariationDto:
        """Create an instance of ComplianceTemplateVariationDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceTemplateVariationDto.parse_obj(obj)

        _obj = ComplianceTemplateVariationDto.parse_obj({
            "label": obj.get("label"),
            "description": obj.get("description"),
            "outcome_description": obj.get("outcomeDescription"),
            "referenced_group_label": obj.get("referencedGroupLabel"),
            "steps": [ComplianceStep.from_dict(_item) for _item in obj.get("steps")] if obj.get("steps") is not None else None
        })
        return _obj
