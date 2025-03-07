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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictBool, constr 

class CdsProtectionDetailSpecification(BaseModel):
    """
    CDSs generally conform to fairly standard definitions, but can be tweaked in a number of different ways.  This class gathers a number of common features which may deviate. These will default to the market standard when  no overrides are provided.  # noqa: E501
    """
    seniority:  StrictStr = Field(...,alias="seniority", description="The seniority level of the CDS.    Supported string (enumeration) values are: [SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2].") 
    restructuring_type:  StrictStr = Field(...,alias="restructuringType", description="The restructuring clause.  Supported string (enumeration) values are: [CR, MR, MM, XR].") 
    protect_start_day: StrictBool = Field(..., alias="protectStartDay", description="Does the protection leg pay out in the case of default on the start date.")
    pay_accrued_interest_on_default: StrictBool = Field(..., alias="payAccruedInterestOnDefault", description="Should accrued interest on the premium leg be paid if a credit event occurs.")
    __properties = ["seniority", "restructuringType", "protectStartDay", "payAccruedInterestOnDefault"]

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
    def from_json(cls, json_str: str) -> CdsProtectionDetailSpecification:
        """Create an instance of CdsProtectionDetailSpecification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CdsProtectionDetailSpecification:
        """Create an instance of CdsProtectionDetailSpecification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CdsProtectionDetailSpecification.parse_obj(obj)

        _obj = CdsProtectionDetailSpecification.parse_obj({
            "seniority": obj.get("seniority"),
            "restructuring_type": obj.get("restructuringType"),
            "protect_start_day": obj.get("protectStartDay"),
            "pay_accrued_interest_on_default": obj.get("payAccruedInterestOnDefault")
        })
        return _obj
