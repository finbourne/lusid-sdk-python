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


from typing import Any, Dict, Optional, Union
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr 

class Touch(BaseModel):
    """
    Touch class for exotic FxOption  # noqa: E501
    """
    direction:  StrictStr = Field(...,alias="direction", description="Supported string (enumeration) values are: [Down, Up].") 
    level: Union[StrictFloat, StrictInt] = Field(..., description="Trigger level, which the underlying should (or should not) cross/touch.")
    monitoring:  Optional[StrictStr] = Field(None,alias="monitoring", description="Supported string (enumeration) values are: [European, Bermudan, American].") 
    type:  StrictStr = Field(...,alias="type", description="Supported string (enumeration) values are: [Touch, Notouch].") 
    __properties = ["direction", "level", "monitoring", "type"]

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
    def from_json(cls, json_str: str) -> Touch:
        """Create an instance of Touch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if monitoring (nullable) is None
        # and __fields_set__ contains the field
        if self.monitoring is None and "monitoring" in self.__fields_set__:
            _dict['monitoring'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Touch:
        """Create an instance of Touch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Touch.parse_obj(obj)

        _obj = Touch.parse_obj({
            "direction": obj.get("direction"),
            "level": obj.get("level"),
            "monitoring": obj.get("monitoring"),
            "type": obj.get("type")
        })
        return _obj
