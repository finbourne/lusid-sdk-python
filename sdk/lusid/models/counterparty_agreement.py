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
from typing import Any, Dict
from pydantic.v1 import StrictStr, Field, BaseModel, Field, constr 
from lusid.models.counterparty_signatory import CounterpartySignatory
from lusid.models.resource_id import ResourceId

class CounterpartyAgreement(BaseModel):
    """
    Represents the legal agreement between two parties engaged in an OTC transaction.  A typical example would be a 2002 ISDA Master Agreement, signed by two legal entities on a given date.  # noqa: E501
    """
    display_name:  StrictStr = Field(...,alias="displayName", description="A user-defined display label for the Counterparty Agreement.") 
    agreement_type:  StrictStr = Field(...,alias="agreementType", description="A user-defined field to capture the type of agreement this represents. Examples might be \"ISDA 2002 Master Agreement\" or \"ISDA 1992 Master Agreement\".") 
    counterparty_signatory: CounterpartySignatory = Field(..., alias="counterpartySignatory")
    dated_as_of: datetime = Field(..., alias="datedAsOf", description="The date on which the CounterpartyAgreement was signed by both parties.")
    credit_support_annex_id: ResourceId = Field(..., alias="creditSupportAnnexId")
    id: ResourceId = Field(...)
    __properties = ["displayName", "agreementType", "counterpartySignatory", "datedAsOf", "creditSupportAnnexId", "id"]

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
    def from_json(cls, json_str: str) -> CounterpartyAgreement:
        """Create an instance of CounterpartyAgreement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of counterparty_signatory
        if self.counterparty_signatory:
            _dict['counterpartySignatory'] = self.counterparty_signatory.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_support_annex_id
        if self.credit_support_annex_id:
            _dict['creditSupportAnnexId'] = self.credit_support_annex_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CounterpartyAgreement:
        """Create an instance of CounterpartyAgreement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CounterpartyAgreement.parse_obj(obj)

        _obj = CounterpartyAgreement.parse_obj({
            "display_name": obj.get("displayName"),
            "agreement_type": obj.get("agreementType"),
            "counterparty_signatory": CounterpartySignatory.from_dict(obj.get("counterpartySignatory")) if obj.get("counterpartySignatory") is not None else None,
            "dated_as_of": obj.get("datedAsOf"),
            "credit_support_annex_id": ResourceId.from_dict(obj.get("creditSupportAnnexId")) if obj.get("creditSupportAnnexId") is not None else None,
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None
        })
        return _obj
