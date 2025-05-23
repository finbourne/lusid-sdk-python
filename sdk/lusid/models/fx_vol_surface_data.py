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
from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, Field, StrictStr, conlist, constr, validator 
from lusid.models.complex_market_data import ComplexMarketData
from lusid.models.lusid_instrument import LusidInstrument
from lusid.models.market_quote import MarketQuote

class FxVolSurfaceData(ComplexMarketData):
    """
    Market Data for an fx vol surface, represented by a list of fx options and corresponding market quotes  # noqa: E501
    """
    base_date: datetime = Field(..., alias="baseDate", description="Base date of the surface")
    instruments: conlist(LusidInstrument) = Field(..., description="The set of instruments that define the surface.")
    quotes: conlist(MarketQuote) = Field(..., description="The set of market quotes that define the surface, in NormalVol or LogNormalVol terms.")
    lineage:  Optional[StrictStr] = Field(None,alias="lineage", description="Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.") 
    market_data_type:  StrictStr = Field(...,alias="marketDataType", description="The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface") 
    additional_properties: Dict[str, Any] = {}
    __properties = ["marketDataType", "baseDate", "instruments", "quotes", "lineage"]

    @validator('market_data_type')
    def market_data_type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'FxVolSurfaceData' not in [ 
                                    # For notification application classes
                                    'AmazonSqsNotificationType',
                                    'AmazonSqsNotificationTypeResponse',
                                    'AmazonSqsPrincipalAuthNotificationType',
                                    'AmazonSqsPrincipalAuthNotificationTypeResponse',
                                    'AzureServiceBusTypeResponse',
                                    'AzureServiceBusNotificationType',
                                    'EmailNotificationType',
                                    'EmailNotificationTypeResponse',
                                    'SmsNotificationType',
                                    'SmsNotificationTypeResponse',
                                    'WebhookNotificationType',
                                    'WebhookNotificationTypeResponse',
                        
                                    # For workflow application classes
                                    'CreateChildTasksAction', 
                                    'RunWorkerAction', 
                                    'TriggerParentTaskAction',
                                    'CreateChildTasksActionResponse', 
                                    'RunWorkerActionResponse',
                                    'TriggerParentTaskActionResponse',
                                    'CreateNewTaskActivity',
                                    'UpdateMatchingTasksActivity',
                                    'CreateNewTaskActivityResponse', 
                                    'UpdateMatchingTasksActivityResponse',
                                    'Fail', 
                                    'GroupReconciliation', 
                                    'HealthCheck', 
                                    'LuminesceView', 
                                    'SchedulerJob', 
                                    'Sleep',
                                    'FailResponse', 
                                    'GroupReconciliationResponse', 
                                    'HealthCheckResponse', 
                                    'LuminesceViewResponse', 
                                    'SchedulerJobResponse', 
                                    'SleepResponse']:
           return value
        
        # Only validate the 'type' property of the class
        if "market_data_type" != "type":
            return value

        if value not in ('DiscountFactorCurveData', 'EquityVolSurfaceData', 'FxVolSurfaceData', 'IrVolCubeData', 'OpaqueMarketData', 'YieldCurveData', 'FxForwardCurveData', 'FxForwardPipsCurveData', 'FxForwardTenorCurveData', 'FxForwardTenorPipsCurveData', 'FxForwardCurveByQuoteReference', 'CreditSpreadCurveData', 'EquityCurveByPricesData', 'ConstantVolatilitySurface'):
            raise ValueError("must be one of enum values ('DiscountFactorCurveData', 'EquityVolSurfaceData', 'FxVolSurfaceData', 'IrVolCubeData', 'OpaqueMarketData', 'YieldCurveData', 'FxForwardCurveData', 'FxForwardPipsCurveData', 'FxForwardTenorCurveData', 'FxForwardTenorPipsCurveData', 'FxForwardCurveByQuoteReference', 'CreditSpreadCurveData', 'EquityCurveByPricesData', 'ConstantVolatilitySurface')")
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
    def from_json(cls, json_str: str) -> FxVolSurfaceData:
        """Create an instance of FxVolSurfaceData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in instruments (list)
        _items = []
        if self.instruments:
            for _item in self.instruments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['instruments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in quotes (list)
        _items = []
        if self.quotes:
            for _item in self.quotes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['quotes'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if lineage (nullable) is None
        # and __fields_set__ contains the field
        if self.lineage is None and "lineage" in self.__fields_set__:
            _dict['lineage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FxVolSurfaceData:
        """Create an instance of FxVolSurfaceData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FxVolSurfaceData.parse_obj(obj)

        _obj = FxVolSurfaceData.parse_obj({
            "market_data_type": obj.get("marketDataType"),
            "base_date": obj.get("baseDate"),
            "instruments": [LusidInstrument.from_dict(_item) for _item in obj.get("instruments")] if obj.get("instruments") is not None else None,
            "quotes": [MarketQuote.from_dict(_item) for _item in obj.get("quotes")] if obj.get("quotes") is not None else None,
            "lineage": obj.get("lineage")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
