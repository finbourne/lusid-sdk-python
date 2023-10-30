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
from pydantic import BaseModel, Field
from lusid.models.flow_conventions import FlowConventions

class UpsertFlowConventionsRequest(BaseModel):
    """
    Flow conventions that is to be stored in the convention data store.  Only one of these must be present.  # noqa: E501
    """
    flow_conventions: Optional[FlowConventions] = Field(None, alias="flowConventions")
    __properties = ["flowConventions"]

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
    def from_json(cls, json_str: str) -> UpsertFlowConventionsRequest:
        """Create an instance of UpsertFlowConventionsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of flow_conventions
        if self.flow_conventions:
            _dict['flowConventions'] = self.flow_conventions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpsertFlowConventionsRequest:
        """Create an instance of UpsertFlowConventionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpsertFlowConventionsRequest.parse_obj(obj)

        _obj = UpsertFlowConventionsRequest.parse_obj({
            "flow_conventions": FlowConventions.from_dict(obj.get("flowConventions")) if obj.get("flowConventions") is not None else None
        })
        return _obj