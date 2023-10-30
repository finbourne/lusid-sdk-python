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
from pydantic import BaseModel, Field, StrictStr, conlist
from lusid.models.link import Link
from lusid.models.model_property import ModelProperty
from lusid.models.portfolio_entity_id import PortfolioEntityId
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class Abor(BaseModel):
    """
    An Abor entity.  # noqa: E501
    """
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    id: ResourceId = Field(...)
    display_name: Optional[StrictStr] = Field(None, alias="displayName", description="The name of the Abor.")
    description: Optional[StrictStr] = Field(None, description="The description for the Abor.")
    portfolio_ids: conlist(PortfolioEntityId) = Field(..., alias="portfolioIds", description="The list with the portfolio ids which are part of the Abor.")
    abor_configuration_id: Optional[ResourceId] = Field(None, alias="aborConfigurationId")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="A set of properties for the Abor.")
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = None
    __properties = ["href", "id", "displayName", "description", "portfolioIds", "aborConfigurationId", "properties", "version", "links"]

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
    def from_json(cls, json_str: str) -> Abor:
        """Create an instance of Abor from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in portfolio_ids (list)
        _items = []
        if self.portfolio_ids:
            for _item in self.portfolio_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['portfolioIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of abor_configuration_id
        if self.abor_configuration_id:
            _dict['aborConfigurationId'] = self.abor_configuration_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
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
        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Abor:
        """Create an instance of Abor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Abor.parse_obj(obj)

        _obj = Abor.parse_obj({
            "href": obj.get("href"),
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "portfolio_ids": [PortfolioEntityId.from_dict(_item) for _item in obj.get("portfolioIds")] if obj.get("portfolioIds") is not None else None,
            "abor_configuration_id": ResourceId.from_dict(obj.get("aborConfigurationId")) if obj.get("aborConfigurationId") is not None else None,
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj