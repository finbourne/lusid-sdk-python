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
from lusid.models.counterparty_agreement import CounterpartyAgreement

class UpsertCounterpartyAgreementRequest(BaseModel):
    """
    Counterparty Agreement that is to be stored in the convention data store.  There must be only one of these present.  # noqa: E501
    """
    counterparty_agreement: CounterpartyAgreement = Field(..., alias="counterpartyAgreement")
    __properties = ["counterpartyAgreement"]

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
    def from_json(cls, json_str: str) -> UpsertCounterpartyAgreementRequest:
        """Create an instance of UpsertCounterpartyAgreementRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of counterparty_agreement
        if self.counterparty_agreement:
            _dict['counterpartyAgreement'] = self.counterparty_agreement.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpsertCounterpartyAgreementRequest:
        """Create an instance of UpsertCounterpartyAgreementRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpsertCounterpartyAgreementRequest.parse_obj(obj)

        _obj = UpsertCounterpartyAgreementRequest.parse_obj({
            "counterparty_agreement": CounterpartyAgreement.from_dict(obj.get("counterpartyAgreement")) if obj.get("counterpartyAgreement") is not None else None
        })
        return _obj
