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
from pydantic.v1 import BaseModel, Field, constr, validator

class TranslationScriptId(BaseModel):
    """
    Id of the Translation Script.  # noqa: E501
    """
    scope: constr(strict=True, max_length=64, min_length=1) = Field(..., description="Scope of the translation script.")
    code: constr(strict=True, max_length=64, min_length=1) = Field(..., description="Code of the translation script.")
    version: constr(strict=True, max_length=30, min_length=1) = Field(..., description="Semantic Version of the translation script of the form MAJOR.MINOR.PATCH.")
    __properties = ["scope", "code", "version"]

    @validator('scope')
    def scope_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('version')
    def version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/")
        return value

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
    def from_json(cls, json_str: str) -> TranslationScriptId:
        """Create an instance of TranslationScriptId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TranslationScriptId:
        """Create an instance of TranslationScriptId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TranslationScriptId.parse_obj(obj)

        _obj = TranslationScriptId.parse_obj({
            "scope": obj.get("scope"),
            "code": obj.get("code"),
            "version": obj.get("version")
        })
        return _obj
