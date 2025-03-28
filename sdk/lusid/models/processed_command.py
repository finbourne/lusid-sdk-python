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
from lusid.models.user import User

class ProcessedCommand(BaseModel):
    """
    The list of commands.  # noqa: E501
    """
    description:  StrictStr = Field(...,alias="description", description="The description of the command issued.") 
    path:  Optional[StrictStr] = Field(None,alias="path", description="The unique identifier for the command including the request id.") 
    user_id: User = Field(..., alias="userId")
    processed_time: datetime = Field(..., alias="processedTime", description="The asAt datetime that the events published by the processing of this command were committed to LUSID.")
    __properties = ["description", "path", "userId", "processedTime"]

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
    def from_json(cls, json_str: str) -> ProcessedCommand:
        """Create an instance of ProcessedCommand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user_id
        if self.user_id:
            _dict['userId'] = self.user_id.to_dict()
        # set to None if path (nullable) is None
        # and __fields_set__ contains the field
        if self.path is None and "path" in self.__fields_set__:
            _dict['path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProcessedCommand:
        """Create an instance of ProcessedCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProcessedCommand.parse_obj(obj)

        _obj = ProcessedCommand.parse_obj({
            "description": obj.get("description"),
            "path": obj.get("path"),
            "user_id": User.from_dict(obj.get("userId")) if obj.get("userId") is not None else None,
            "processed_time": obj.get("processedTime")
        })
        return _obj
