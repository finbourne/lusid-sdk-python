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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, constr, validator 

class CreateRelationshipDefinitionRequest(BaseModel):
    """
    CreateRelationshipDefinitionRequest
    """
    scope:  StrictStr = Field(...,alias="scope", description="The scope that the relationship definition exists in.") 
    code:  StrictStr = Field(...,alias="code", description="The code of the relationship definition. Together with the scope this uniquely defines the relationship definition.") 
    source_entity_type:  StrictStr = Field(...,alias="sourceEntityType", description="The entity type of the source entity object. Allowed values are 'Portfolio', 'PortfolioGroup', 'Person', 'LegalEntity', 'Instrument' or a custom entity type prefixed with '~'.") 
    target_entity_type:  StrictStr = Field(...,alias="targetEntityType", description="The entity type of the target entity object. Allowed values are 'Portfolio', 'PortfolioGroup', 'Person', 'LegalEntity', 'Instrument' or a custom entity type prefixed with '~'.") 
    display_name:  StrictStr = Field(...,alias="displayName", description="The display name of the relationship definition.") 
    outward_description:  StrictStr = Field(...,alias="outwardDescription", description="The description to relate source entity object and target entity object.") 
    inward_description:  StrictStr = Field(...,alias="inwardDescription", description="The description to relate target entity object and source entity object.") 
    life_time:  Optional[StrictStr] = Field(None,alias="lifeTime", description="Describes how the relationships can change over time. Allowed values are 'Perpetual' and 'TimeVariant', defaults to 'Perpetual' if not specified.") 
    relationship_cardinality:  Optional[StrictStr] = Field(None,alias="relationshipCardinality", description="Describes the cardinality of the relationship with a specific source entity object and relationships under this definition. Allowed values are 'ManyToMany' and 'ManyToOne', defaults to 'ManyToMany' if not specified.") 
    __properties = ["scope", "code", "sourceEntityType", "targetEntityType", "displayName", "outwardDescription", "inwardDescription", "lifeTime", "relationshipCardinality"]

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
    def from_json(cls, json_str: str) -> CreateRelationshipDefinitionRequest:
        """Create an instance of CreateRelationshipDefinitionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if life_time (nullable) is None
        # and __fields_set__ contains the field
        if self.life_time is None and "life_time" in self.__fields_set__:
            _dict['lifeTime'] = None

        # set to None if relationship_cardinality (nullable) is None
        # and __fields_set__ contains the field
        if self.relationship_cardinality is None and "relationship_cardinality" in self.__fields_set__:
            _dict['relationshipCardinality'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateRelationshipDefinitionRequest:
        """Create an instance of CreateRelationshipDefinitionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateRelationshipDefinitionRequest.parse_obj(obj)

        _obj = CreateRelationshipDefinitionRequest.parse_obj({
            "scope": obj.get("scope"),
            "code": obj.get("code"),
            "source_entity_type": obj.get("sourceEntityType"),
            "target_entity_type": obj.get("targetEntityType"),
            "display_name": obj.get("displayName"),
            "outward_description": obj.get("outwardDescription"),
            "inward_description": obj.get("inwardDescription"),
            "life_time": obj.get("lifeTime"),
            "relationship_cardinality": obj.get("relationshipCardinality")
        })
        return _obj
