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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
from lusid.models.compliance_template_variation_dto import ComplianceTemplateVariationDto
from lusid.models.link import Link
from lusid.models.model_property import ModelProperty
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class ComplianceRuleTemplate(BaseModel):
    """
    ComplianceRuleTemplate
    """
    id: Optional[ResourceId] = None
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="The description of the Compliance Template")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="Properties associated with the Compliance Template Variation")
    variations: Optional[conlist(ComplianceTemplateVariationDto)] = Field(None, description="Variation details of a Compliance Template")
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime.")
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = None
    __properties = ["id", "description", "properties", "variations", "href", "version", "links"]

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

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
    def from_json(cls, json_str: str) -> ComplianceRuleTemplate:
        """Create an instance of ComplianceRuleTemplate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in variations (list)
        _items = []
        if self.variations:
            for _item in self.variations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variations'] = _items
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if variations (nullable) is None
        # and __fields_set__ contains the field
        if self.variations is None and "variations" in self.__fields_set__:
            _dict['variations'] = None

        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceRuleTemplate:
        """Create an instance of ComplianceRuleTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceRuleTemplate.parse_obj(obj)

        _obj = ComplianceRuleTemplate.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "description": obj.get("description"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "variations": [ComplianceTemplateVariationDto.from_dict(_item) for _item in obj.get("variations")] if obj.get("variations") is not None else None,
            "href": obj.get("href"),
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj