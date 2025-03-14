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
from pydantic.v1 import StrictStr, Field, BaseModel, Field 
from lusid.models.resource_id import ResourceId

class CancelOrdersAndMoveRemainingRequest(BaseModel):
    """
    A request to create or update a Order.  # noqa: E501
    """
    cancel_order_id: ResourceId = Field(..., alias="cancelOrderId")
    move_remaining_to_order_id: ResourceId = Field(..., alias="moveRemainingToOrderId")
    move_remaining_to_block_id: ResourceId = Field(..., alias="moveRemainingToBlockId")
    __properties = ["cancelOrderId", "moveRemainingToOrderId", "moveRemainingToBlockId"]

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
    def from_json(cls, json_str: str) -> CancelOrdersAndMoveRemainingRequest:
        """Create an instance of CancelOrdersAndMoveRemainingRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cancel_order_id
        if self.cancel_order_id:
            _dict['cancelOrderId'] = self.cancel_order_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of move_remaining_to_order_id
        if self.move_remaining_to_order_id:
            _dict['moveRemainingToOrderId'] = self.move_remaining_to_order_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of move_remaining_to_block_id
        if self.move_remaining_to_block_id:
            _dict['moveRemainingToBlockId'] = self.move_remaining_to_block_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CancelOrdersAndMoveRemainingRequest:
        """Create an instance of CancelOrdersAndMoveRemainingRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CancelOrdersAndMoveRemainingRequest.parse_obj(obj)

        _obj = CancelOrdersAndMoveRemainingRequest.parse_obj({
            "cancel_order_id": ResourceId.from_dict(obj.get("cancelOrderId")) if obj.get("cancelOrderId") is not None else None,
            "move_remaining_to_order_id": ResourceId.from_dict(obj.get("moveRemainingToOrderId")) if obj.get("moveRemainingToOrderId") is not None else None,
            "move_remaining_to_block_id": ResourceId.from_dict(obj.get("moveRemainingToBlockId")) if obj.get("moveRemainingToBlockId") is not None else None
        })
        return _obj
