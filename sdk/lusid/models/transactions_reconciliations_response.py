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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist 
from lusid.models.mapping import Mapping
from lusid.models.reconciled_transaction import ReconciledTransaction

class TransactionsReconciliationsResponse(BaseModel):
    """
    TransactionsReconciliationsResponse
    """
    mapping: Optional[Mapping] = None
    data: Optional[conlist(ReconciledTransaction)] = Field(None, description="The result of this reconciliation")
    __properties = ["mapping", "data"]

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
    def from_json(cls, json_str: str) -> TransactionsReconciliationsResponse:
        """Create an instance of TransactionsReconciliationsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of mapping
        if self.mapping:
            _dict['mapping'] = self.mapping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionsReconciliationsResponse:
        """Create an instance of TransactionsReconciliationsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionsReconciliationsResponse.parse_obj(obj)

        _obj = TransactionsReconciliationsResponse.parse_obj({
            "mapping": Mapping.from_dict(obj.get("mapping")) if obj.get("mapping") is not None else None,
            "data": [ReconciledTransaction.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None
        })
        return _obj
