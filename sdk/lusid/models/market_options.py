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


from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictBool, constr, validator 

class MarketOptions(BaseModel):
    """
    The set of options that control miscellaneous and default market resolution behaviour.  These are aimed at a 'crude' level of control for those who do not wish to fine tune the way that data is resolved.  For clients who wish to simply match instruments to prices this is quite possibly sufficient. For those wishing to control market data sources  according to requirements based on accuracy or timeliness it is not. In more advanced cases the options should largely be ignored and rules specified  per source. Be aware that where no specified rule matches the final fallback is on to the logic implied here.  # noqa: E501
    """
    default_supplier:  Optional[StrictStr] = Field(None,alias="defaultSupplier", description="The default supplier of data. This controls which 'dialect' is used to find particular market data. e.g. one supplier might address data by RIC, another by PermId") 
    default_instrument_code_type:  Optional[StrictStr] = Field(None,alias="defaultInstrumentCodeType", description="When instrument quotes are searched for, what identifier should be used by default") 
    default_scope:  StrictStr = Field(...,alias="defaultScope", description="For default rules, which scope should data be searched for in") 
    attempt_to_infer_missing_fx: Optional[StrictBool] = Field(None, alias="attemptToInferMissingFx", description="if true will calculate a missing Fx pair (e.g. THBJPY) from the inverse JPYTHB or from standardised pairs against USD, e.g. THBUSD and JPYUSD")
    calendar_scope:  Optional[StrictStr] = Field(None,alias="calendarScope", description="The scope in which holiday calendars stored") 
    convention_scope:  Optional[StrictStr] = Field(None,alias="conventionScope", description="The scope in which conventions stored") 
    __properties = ["defaultSupplier", "defaultInstrumentCodeType", "defaultScope", "attemptToInferMissingFx", "calendarScope", "conventionScope"]

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
    def from_json(cls, json_str: str) -> MarketOptions:
        """Create an instance of MarketOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if default_supplier (nullable) is None
        # and __fields_set__ contains the field
        if self.default_supplier is None and "default_supplier" in self.__fields_set__:
            _dict['defaultSupplier'] = None

        # set to None if default_instrument_code_type (nullable) is None
        # and __fields_set__ contains the field
        if self.default_instrument_code_type is None and "default_instrument_code_type" in self.__fields_set__:
            _dict['defaultInstrumentCodeType'] = None

        # set to None if calendar_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.calendar_scope is None and "calendar_scope" in self.__fields_set__:
            _dict['calendarScope'] = None

        # set to None if convention_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.convention_scope is None and "convention_scope" in self.__fields_set__:
            _dict['conventionScope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MarketOptions:
        """Create an instance of MarketOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MarketOptions.parse_obj(obj)

        _obj = MarketOptions.parse_obj({
            "default_supplier": obj.get("defaultSupplier"),
            "default_instrument_code_type": obj.get("defaultInstrumentCodeType"),
            "default_scope": obj.get("defaultScope"),
            "attempt_to_infer_missing_fx": obj.get("attemptToInferMissingFx"),
            "calendar_scope": obj.get("calendarScope"),
            "convention_scope": obj.get("conventionScope")
        })
        return _obj
