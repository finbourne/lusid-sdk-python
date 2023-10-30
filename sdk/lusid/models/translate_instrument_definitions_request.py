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
from pydantic import BaseModel, Field, constr, validator
from lusid.models.lusid_instrument import LusidInstrument

class TranslateInstrumentDefinitionsRequest(BaseModel):
    """
    A collection of instruments to translate, along with the target dialect to translate into.  # noqa: E501
    """
    instruments: Dict[str, LusidInstrument] = Field(..., description="The collection of instruments to translate.                Each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument.")
    dialect: constr(strict=True, max_length=256, min_length=1) = Field(..., description="The target dialect that the given instruments should be translated to.")
    __properties = ["instruments", "dialect"]

    @validator('dialect')
    def dialect_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z]*$/")
        return value

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
    def from_json(cls, json_str: str) -> TranslateInstrumentDefinitionsRequest:
        """Create an instance of TranslateInstrumentDefinitionsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in instruments (dict)
        _field_dict = {}
        if self.instruments:
            for _key in self.instruments:
                if self.instruments[_key]:
                    _field_dict[_key] = self.instruments[_key].to_dict()
            _dict['instruments'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TranslateInstrumentDefinitionsRequest:
        """Create an instance of TranslateInstrumentDefinitionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TranslateInstrumentDefinitionsRequest.parse_obj(obj)

        _obj = TranslateInstrumentDefinitionsRequest.parse_obj({
            "instruments": dict(
                (_k, LusidInstrument.from_dict(_v))
                for _k, _v in obj.get("instruments").items()
            )
            if obj.get("instruments") is not None
            else None,
            "dialect": obj.get("dialect")
        })
        return _obj