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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist 
from lusid.models.compliance_rule_result import ComplianceRuleResult
from lusid.models.resource_id import ResourceId

class ComplianceBreachedOrderInfo(BaseModel):
    """
    ComplianceBreachedOrderInfo
    """
    order_id: ResourceId = Field(..., alias="orderId")
    list_rule_result: conlist(ComplianceRuleResult) = Field(..., alias="listRuleResult", description="The Rule Results for a particular compliance run")
    __properties = ["orderId", "listRuleResult"]

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
    def from_json(cls, json_str: str) -> ComplianceBreachedOrderInfo:
        """Create an instance of ComplianceBreachedOrderInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of order_id
        if self.order_id:
            _dict['orderId'] = self.order_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in list_rule_result (list)
        _items = []
        if self.list_rule_result:
            for _item in self.list_rule_result:
                if _item:
                    _items.append(_item.to_dict())
            _dict['listRuleResult'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceBreachedOrderInfo:
        """Create an instance of ComplianceBreachedOrderInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceBreachedOrderInfo.parse_obj(obj)

        _obj = ComplianceBreachedOrderInfo.parse_obj({
            "order_id": ResourceId.from_dict(obj.get("orderId")) if obj.get("orderId") is not None else None,
            "list_rule_result": [ComplianceRuleResult.from_dict(_item) for _item in obj.get("listRuleResult")] if obj.get("listRuleResult") is not None else None
        })
        return _obj
