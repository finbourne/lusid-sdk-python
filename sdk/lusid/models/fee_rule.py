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


from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist, constr 
from lusid.models.calculation_info import CalculationInfo
from lusid.models.link import Link
from lusid.models.version import Version

class FeeRule(BaseModel):
    """
    FeeRule
    """
    code:  StrictStr = Field(...,alias="code", description="") 
    transaction_property_key:  StrictStr = Field(...,alias="transactionPropertyKey", description="") 
    transaction_type:  StrictStr = Field(...,alias="transactionType", description="") 
    country:  StrictStr = Field(...,alias="country", description="") 
    counterparty:  StrictStr = Field(...,alias="counterparty", description="") 
    transaction_currency:  StrictStr = Field(...,alias="transactionCurrency", description="") 
    settlement_currency:  StrictStr = Field(...,alias="settlementCurrency", description="") 
    execution_broker:  StrictStr = Field(...,alias="executionBroker", description="") 
    custodian:  StrictStr = Field(...,alias="custodian", description="") 
    exchange:  StrictStr = Field(...,alias="exchange", description="") 
    fee: CalculationInfo = Field(...)
    min_fee: Optional[CalculationInfo] = Field(None, alias="minFee")
    max_fee: Optional[CalculationInfo] = Field(None, alias="maxFee")
    additional_keys: Optional[Dict[str, StrictStr]] = Field(None, alias="additionalKeys")
    description:  Optional[StrictStr] = Field(None,alias="description", description="") 
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = None
    __properties = ["code", "transactionPropertyKey", "transactionType", "country", "counterparty", "transactionCurrency", "settlementCurrency", "executionBroker", "custodian", "exchange", "fee", "minFee", "maxFee", "additionalKeys", "description", "version", "links"]

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
    def from_json(cls, json_str: str) -> FeeRule:
        """Create an instance of FeeRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of min_fee
        if self.min_fee:
            _dict['minFee'] = self.min_fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_fee
        if self.max_fee:
            _dict['maxFee'] = self.max_fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if additional_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.additional_keys is None and "additional_keys" in self.__fields_set__:
            _dict['additionalKeys'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FeeRule:
        """Create an instance of FeeRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FeeRule.parse_obj(obj)

        _obj = FeeRule.parse_obj({
            "code": obj.get("code"),
            "transaction_property_key": obj.get("transactionPropertyKey"),
            "transaction_type": obj.get("transactionType"),
            "country": obj.get("country"),
            "counterparty": obj.get("counterparty"),
            "transaction_currency": obj.get("transactionCurrency"),
            "settlement_currency": obj.get("settlementCurrency"),
            "execution_broker": obj.get("executionBroker"),
            "custodian": obj.get("custodian"),
            "exchange": obj.get("exchange"),
            "fee": CalculationInfo.from_dict(obj.get("fee")) if obj.get("fee") is not None else None,
            "min_fee": CalculationInfo.from_dict(obj.get("minFee")) if obj.get("minFee") is not None else None,
            "max_fee": CalculationInfo.from_dict(obj.get("maxFee")) if obj.get("maxFee") is not None else None,
            "additional_keys": obj.get("additionalKeys"),
            "description": obj.get("description"),
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
