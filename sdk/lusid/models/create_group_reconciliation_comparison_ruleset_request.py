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


from typing import Any, Dict, List
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist, constr 
from lusid.models.group_reconciliation_aggregate_attribute_rule import GroupReconciliationAggregateAttributeRule
from lusid.models.group_reconciliation_core_attribute_rule import GroupReconciliationCoreAttributeRule
from lusid.models.resource_id import ResourceId

class CreateGroupReconciliationComparisonRulesetRequest(BaseModel):
    """
    CreateGroupReconciliationComparisonRulesetRequest
    """
    id: ResourceId = Field(...)
    display_name:  StrictStr = Field(...,alias="displayName", description="The name of the ruleset") 
    reconciliation_type:  StrictStr = Field(...,alias="reconciliationType", description="The type of reconciliation to perform. \"Holding\" | \"Transaction\" | \"Valuation\"") 
    core_attribute_rules: conlist(GroupReconciliationCoreAttributeRule) = Field(..., alias="coreAttributeRules", description="The core comparison rules")
    aggregate_attribute_rules: conlist(GroupReconciliationAggregateAttributeRule) = Field(..., alias="aggregateAttributeRules", description="The aggregate comparison rules")
    __properties = ["id", "displayName", "reconciliationType", "coreAttributeRules", "aggregateAttributeRules"]

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
    def from_json(cls, json_str: str) -> CreateGroupReconciliationComparisonRulesetRequest:
        """Create an instance of CreateGroupReconciliationComparisonRulesetRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in core_attribute_rules (list)
        _items = []
        if self.core_attribute_rules:
            for _item in self.core_attribute_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['coreAttributeRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in aggregate_attribute_rules (list)
        _items = []
        if self.aggregate_attribute_rules:
            for _item in self.aggregate_attribute_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['aggregateAttributeRules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateGroupReconciliationComparisonRulesetRequest:
        """Create an instance of CreateGroupReconciliationComparisonRulesetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateGroupReconciliationComparisonRulesetRequest.parse_obj(obj)

        _obj = CreateGroupReconciliationComparisonRulesetRequest.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "display_name": obj.get("displayName"),
            "reconciliation_type": obj.get("reconciliationType"),
            "core_attribute_rules": [GroupReconciliationCoreAttributeRule.from_dict(_item) for _item in obj.get("coreAttributeRules")] if obj.get("coreAttributeRules") is not None else None,
            "aggregate_attribute_rules": [GroupReconciliationAggregateAttributeRule.from_dict(_item) for _item in obj.get("aggregateAttributeRules")] if obj.get("aggregateAttributeRules") is not None else None
        })
        return _obj
