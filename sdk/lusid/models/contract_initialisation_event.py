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
from typing import Any, Dict, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from lusid.models.contract_details import ContractDetails
from lusid.models.instrument_event import InstrumentEvent

class ContractInitialisationEvent(InstrumentEvent):
    """
    Event to initialise a contract with a given limit against a LoanFacility.  # noqa: E501
    """
    limit: Union[StrictFloat, StrictInt] = Field(..., description="Limit of this contract.  Must be positive.")
    var_date: datetime = Field(..., alias="date", description="Initialisation date of the contract.")
    contract_details: ContractDetails = Field(..., alias="contractDetails")
    instrument_event_type: StrictStr = Field(..., alias="instrumentEventType", description="The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentEventType", "limit", "date", "contractDetails"]

    @validator('instrument_event_type')
    def instrument_event_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent', 'MergerEvent', 'FutureExpiryEvent', 'SwapCashFlowEvent', 'SwapPrincipalEvent', 'CreditPremiumCashFlowEvent', 'CdsCreditEvent', 'CdxCreditEvent', 'MbsCouponEvent', 'MbsPrincipalEvent', 'BonusIssueEvent', 'MbsPrincipalWriteOffEvent', 'MbsInterestDeferralEvent', 'MbsInterestShortfallEvent', 'TenderEvent', 'CallOnIntermediateSecuritiesEvent', 'IntermediateSecuritiesDistributionEvent', 'OptionExercisePhysicalEvent', 'OptionExerciseCashEvent', 'ProtectionPayoutCashFlowEvent', 'TermDepositInterestEvent', 'TermDepositPrincipalEvent', 'EarlyRedemptionEvent', 'FutureMarkToMarketEvent', 'AdjustGlobalCommitmentEvent', 'ContractInitialisationEvent', 'DrawdownEvent', 'LoanInterestRepaymentEvent'):
            raise ValueError("must be one of enum values ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent', 'MergerEvent', 'FutureExpiryEvent', 'SwapCashFlowEvent', 'SwapPrincipalEvent', 'CreditPremiumCashFlowEvent', 'CdsCreditEvent', 'CdxCreditEvent', 'MbsCouponEvent', 'MbsPrincipalEvent', 'BonusIssueEvent', 'MbsPrincipalWriteOffEvent', 'MbsInterestDeferralEvent', 'MbsInterestShortfallEvent', 'TenderEvent', 'CallOnIntermediateSecuritiesEvent', 'IntermediateSecuritiesDistributionEvent', 'OptionExercisePhysicalEvent', 'OptionExerciseCashEvent', 'ProtectionPayoutCashFlowEvent', 'TermDepositInterestEvent', 'TermDepositPrincipalEvent', 'EarlyRedemptionEvent', 'FutureMarkToMarketEvent', 'AdjustGlobalCommitmentEvent', 'ContractInitialisationEvent', 'DrawdownEvent', 'LoanInterestRepaymentEvent')")
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
    def from_json(cls, json_str: str) -> ContractInitialisationEvent:
        """Create an instance of ContractInitialisationEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of contract_details
        if self.contract_details:
            _dict['contractDetails'] = self.contract_details.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContractInitialisationEvent:
        """Create an instance of ContractInitialisationEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContractInitialisationEvent.parse_obj(obj)

        _obj = ContractInitialisationEvent.parse_obj({
            "instrument_event_type": obj.get("instrumentEventType"),
            "limit": obj.get("limit"),
            "var_date": obj.get("date"),
            "contract_details": ContractDetails.from_dict(obj.get("contractDetails")) if obj.get("contractDetails") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj