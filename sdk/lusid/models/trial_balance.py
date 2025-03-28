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
from lusid.models.link import Link
from lusid.models.model_property import ModelProperty
from lusid.models.multi_currency_amounts import MultiCurrencyAmounts

class TrialBalance(BaseModel):
    """
    A TrialBalance entity.  # noqa: E501
    """
    general_ledger_account_code:  StrictStr = Field(...,alias="generalLedgerAccountCode", description="The Account code that the trial balance results have been grouped against.") 
    description:  Optional[StrictStr] = Field(None,alias="description", description="The description of the record.") 
    levels: conlist(StrictStr) = Field(..., description="The levels that have been derived from the specified General Ledger Profile.")
    account_type:  StrictStr = Field(...,alias="accountType", description="The account type attributed to the record.") 
    local_currency:  StrictStr = Field(...,alias="localCurrency", description="The local currency for the amounts specified. Defaults to base currency if multiple different currencies present in the grouped line.") 
    opening: MultiCurrencyAmounts = Field(...)
    closing: MultiCurrencyAmounts = Field(...)
    debit: MultiCurrencyAmounts = Field(...)
    credit: MultiCurrencyAmounts = Field(...)
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="Properties found on the mapped 'Account', as specified in request.")
    links: Optional[conlist(Link)] = None
    __properties = ["generalLedgerAccountCode", "description", "levels", "accountType", "localCurrency", "opening", "closing", "debit", "credit", "properties", "links"]

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
    def from_json(cls, json_str: str) -> TrialBalance:
        """Create an instance of TrialBalance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of opening
        if self.opening:
            _dict['opening'] = self.opening.to_dict()
        # override the default output from pydantic by calling `to_dict()` of closing
        if self.closing:
            _dict['closing'] = self.closing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of debit
        if self.debit:
            _dict['debit'] = self.debit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit
        if self.credit:
            _dict['credit'] = self.credit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrialBalance:
        """Create an instance of TrialBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrialBalance.parse_obj(obj)

        _obj = TrialBalance.parse_obj({
            "general_ledger_account_code": obj.get("generalLedgerAccountCode"),
            "description": obj.get("description"),
            "levels": obj.get("levels"),
            "account_type": obj.get("accountType"),
            "local_currency": obj.get("localCurrency"),
            "opening": MultiCurrencyAmounts.from_dict(obj.get("opening")) if obj.get("opening") is not None else None,
            "closing": MultiCurrencyAmounts.from_dict(obj.get("closing")) if obj.get("closing") is not None else None,
            "debit": MultiCurrencyAmounts.from_dict(obj.get("debit")) if obj.get("debit") is not None else None,
            "credit": MultiCurrencyAmounts.from_dict(obj.get("credit")) if obj.get("credit") is not None else None,
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
