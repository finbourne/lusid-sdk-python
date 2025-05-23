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
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import StrictStr, Field, Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator 
from lusid.models.complex_market_data import ComplexMarketData
from lusid.models.market_data_options import MarketDataOptions

class FxForwardCurveData(ComplexMarketData):
    """
    Contains data (i.e. dates and rates + metadata) for building fx forward curves  # noqa: E501
    """
    base_date: datetime = Field(..., alias="baseDate", description="EffectiveAt date of the quoted rates")
    dom_ccy:  StrictStr = Field(...,alias="domCcy", description="Domestic currency of the fx forward") 
    fgn_ccy:  StrictStr = Field(...,alias="fgnCcy", description="Foreign currency of the fx forward") 
    dates: conlist(datetime) = Field(..., description="Dates for which the forward rates apply")
    rates: conlist(Union[StrictFloat, StrictInt]) = Field(..., description="Rates provided for the fx forward (price in FgnCcy per unit of DomCcy)")
    lineage:  Optional[StrictStr] = Field(None,alias="lineage", description="Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.") 
    market_data_options: Optional[MarketDataOptions] = Field(None, alias="marketDataOptions")
    market_data_type:  StrictStr = Field(...,alias="marketDataType", description="The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface") 
    additional_properties: Dict[str, Any] = {}
    __properties = ["marketDataType", "baseDate", "domCcy", "fgnCcy", "dates", "rates", "lineage", "marketDataOptions"]

    @validator('market_data_type')
    def market_data_type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'FxForwardCurveData' not in [ 
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
    def from_json(cls, json_str: str) -> FxForwardCurveData:
        """Create an instance of FxForwardCurveData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of market_data_options
        if self.market_data_options:
            _dict['marketDataOptions'] = self.market_data_options.to_dict()
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
    def from_dict(cls, obj: dict) -> FxForwardCurveData:
        """Create an instance of FxForwardCurveData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FxForwardCurveData.parse_obj(obj)

        _obj = FxForwardCurveData.parse_obj({
            "market_data_type": obj.get("marketDataType"),
            "base_date": obj.get("baseDate"),
            "dom_ccy": obj.get("domCcy"),
            "fgn_ccy": obj.get("fgnCcy"),
            "dates": obj.get("dates"),
            "rates": obj.get("rates"),
            "lineage": obj.get("lineage"),
            "market_data_options": MarketDataOptions.from_dict(obj.get("marketDataOptions")) if obj.get("marketDataOptions") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
