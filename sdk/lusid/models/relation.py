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
from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, constr 
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class Relation(BaseModel):
    """
    Representation of a Relation between a requested entity with the stated entity as RelationedEntityId  # noqa: E501
    """
    version: Optional[Version] = None
    relation_definition_id: ResourceId = Field(..., alias="relationDefinitionId")
    related_entity_id: Dict[str, StrictStr] = Field(..., alias="relatedEntityId")
    traversal_direction:  StrictStr = Field(...,alias="traversalDirection") 
    traversal_description:  StrictStr = Field(...,alias="traversalDescription") 
    effective_from: Optional[datetime] = Field(None, alias="effectiveFrom")
    __properties = ["version", "relationDefinitionId", "relatedEntityId", "traversalDirection", "traversalDescription", "effectiveFrom"]

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
    def from_json(cls, json_str: str) -> Relation:
        """Create an instance of Relation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relation_definition_id
        if self.relation_definition_id:
            _dict['relationDefinitionId'] = self.relation_definition_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Relation:
        """Create an instance of Relation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Relation.parse_obj(obj)

        _obj = Relation.parse_obj({
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "relation_definition_id": ResourceId.from_dict(obj.get("relationDefinitionId")) if obj.get("relationDefinitionId") is not None else None,
            "related_entity_id": obj.get("relatedEntityId"),
            "traversal_direction": obj.get("traversalDirection"),
            "traversal_description": obj.get("traversalDescription"),
            "effective_from": obj.get("effectiveFrom")
        })
        return _obj
