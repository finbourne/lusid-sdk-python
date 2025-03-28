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
from lusid.models.side_configuration_data_request import SideConfigurationDataRequest
from lusid.models.transaction_configuration_data_request import TransactionConfigurationDataRequest

class TransactionSetConfigurationDataRequest(BaseModel):
    """
    A bundle of requests to configure a set of transaction types.  # noqa: E501
    """
    transaction_config_requests: conlist(TransactionConfigurationDataRequest) = Field(..., alias="transactionConfigRequests", description="Collection of transaction type models")
    side_config_requests: Optional[conlist(SideConfigurationDataRequest)] = Field(None, alias="sideConfigRequests", description="Collection of side definition requests.")
    __properties = ["transactionConfigRequests", "sideConfigRequests"]

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
    def from_json(cls, json_str: str) -> TransactionSetConfigurationDataRequest:
        """Create an instance of TransactionSetConfigurationDataRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in transaction_config_requests (list)
        _items = []
        if self.transaction_config_requests:
            for _item in self.transaction_config_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactionConfigRequests'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in side_config_requests (list)
        _items = []
        if self.side_config_requests:
            for _item in self.side_config_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sideConfigRequests'] = _items
        # set to None if side_config_requests (nullable) is None
        # and __fields_set__ contains the field
        if self.side_config_requests is None and "side_config_requests" in self.__fields_set__:
            _dict['sideConfigRequests'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionSetConfigurationDataRequest:
        """Create an instance of TransactionSetConfigurationDataRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionSetConfigurationDataRequest.parse_obj(obj)

        _obj = TransactionSetConfigurationDataRequest.parse_obj({
            "transaction_config_requests": [TransactionConfigurationDataRequest.from_dict(_item) for _item in obj.get("transactionConfigRequests")] if obj.get("transactionConfigRequests") is not None else None,
            "side_config_requests": [SideConfigurationDataRequest.from_dict(_item) for _item in obj.get("sideConfigRequests")] if obj.get("sideConfigRequests") is not None else None
        })
        return _obj
