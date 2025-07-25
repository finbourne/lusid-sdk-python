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
from pydantic.v1 import StrictStr, Field, Field, StrictFloat, StrictInt, StrictStr, conlist, validator 
from lusid.models.cash_offer_election import CashOfferElection
from lusid.models.instrument_event import InstrumentEvent
from lusid.models.lapse_election import LapseElection
from lusid.models.tender_offer_election import TenderOfferElection

class RepurchaseOfferEvent(InstrumentEvent):
    """
    Representation of a repurchase offer corporate action.  Represents an offer by the issuer to repurchase its own shares from a shareholder at a given price.  # noqa: E501
    """
    payment_date: Optional[datetime] = Field(None, alias="paymentDate", description="Payment date of the event.")
    market_deadline_date: Optional[datetime] = Field(None, alias="marketDeadlineDate", description="Date set by the issuer or by an agent of the issuer as the latest date to respond to the offer. Must be before or equal to the PaymentDate.")
    repurchase_quantity: Union[StrictFloat, StrictInt] = Field(..., alias="repurchaseQuantity", description="Quantity of the security to be repurchased.")
    cash_offer_elections: conlist(CashOfferElection) = Field(..., alias="cashOfferElections", description="List of possible CashOfferElections for this event. Only 1 should be provided.")
    lapse_elections: conlist(LapseElection) = Field(..., alias="lapseElections", description="List of possible LapseElections for this event. Only 1 should be provided.  Allows the user to opt out of the offer.")
    tender_offer_elections: conlist(TenderOfferElection) = Field(..., alias="tenderOfferElections", description="List of possible TenderOfferElections for this event. Only 1 should be provided.")
    proration_rate: Optional[Union[StrictFloat, StrictInt]] = Field(1, alias="prorationRate", description="The fraction used to calculate a proportional adjustment for RepurchaseQuantity when a full period is not used.  Defaults to 1 if not set. Must be greater than 0 and less than or equal to 1.")
    response_deadline_date: Optional[datetime] = Field(None, alias="responseDeadlineDate", description="Date set by the account servicer as the latest date to respond to the offer.  Optional. If set, must be before or equal to MarketDeadlineDate.  Defaults to MarketDeadlineDate if not set.")
    instrument_event_type:  StrictStr = Field(...,alias="instrumentEventType", description="The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent") 
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentEventType", "paymentDate", "marketDeadlineDate", "repurchaseQuantity", "cashOfferElections", "lapseElections", "tenderOfferElections", "prorationRate", "responseDeadlineDate"]

    @validator('instrument_event_type')
    def instrument_event_type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'RepurchaseOfferEvent' not in [ 
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
        if "instrument_event_type" != "type":
            return value

        if value not in ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent', 'MergerEvent', 'FutureExpiryEvent', 'SwapCashFlowEvent', 'SwapPrincipalEvent', 'CreditPremiumCashFlowEvent', 'CdsCreditEvent', 'CdxCreditEvent', 'MbsCouponEvent', 'MbsPrincipalEvent', 'BonusIssueEvent', 'MbsPrincipalWriteOffEvent', 'MbsInterestDeferralEvent', 'MbsInterestShortfallEvent', 'TenderEvent', 'CallOnIntermediateSecuritiesEvent', 'IntermediateSecuritiesDistributionEvent', 'OptionExercisePhysicalEvent', 'OptionExerciseCashEvent', 'ProtectionPayoutCashFlowEvent', 'TermDepositInterestEvent', 'TermDepositPrincipalEvent', 'EarlyRedemptionEvent', 'FutureMarkToMarketEvent', 'AdjustGlobalCommitmentEvent', 'ContractInitialisationEvent', 'DrawdownEvent', 'LoanInterestRepaymentEvent', 'UpdateDepositAmountEvent', 'LoanPrincipalRepaymentEvent', 'DepositInterestPaymentEvent', 'DepositCloseEvent', 'LoanFacilityContractRolloverEvent', 'RepurchaseOfferEvent', 'RepoPartialClosureEvent', 'RepoCashFlowEvent', 'FlexibleRepoInterestPaymentEvent', 'FlexibleRepoCashFlowEvent', 'FlexibleRepoCollateralEvent', 'ConversionEvent'):
            raise ValueError("must be one of enum values ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent', 'MergerEvent', 'FutureExpiryEvent', 'SwapCashFlowEvent', 'SwapPrincipalEvent', 'CreditPremiumCashFlowEvent', 'CdsCreditEvent', 'CdxCreditEvent', 'MbsCouponEvent', 'MbsPrincipalEvent', 'BonusIssueEvent', 'MbsPrincipalWriteOffEvent', 'MbsInterestDeferralEvent', 'MbsInterestShortfallEvent', 'TenderEvent', 'CallOnIntermediateSecuritiesEvent', 'IntermediateSecuritiesDistributionEvent', 'OptionExercisePhysicalEvent', 'OptionExerciseCashEvent', 'ProtectionPayoutCashFlowEvent', 'TermDepositInterestEvent', 'TermDepositPrincipalEvent', 'EarlyRedemptionEvent', 'FutureMarkToMarketEvent', 'AdjustGlobalCommitmentEvent', 'ContractInitialisationEvent', 'DrawdownEvent', 'LoanInterestRepaymentEvent', 'UpdateDepositAmountEvent', 'LoanPrincipalRepaymentEvent', 'DepositInterestPaymentEvent', 'DepositCloseEvent', 'LoanFacilityContractRolloverEvent', 'RepurchaseOfferEvent', 'RepoPartialClosureEvent', 'RepoCashFlowEvent', 'FlexibleRepoInterestPaymentEvent', 'FlexibleRepoCashFlowEvent', 'FlexibleRepoCollateralEvent', 'ConversionEvent')")
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
    def from_json(cls, json_str: str) -> RepurchaseOfferEvent:
        """Create an instance of RepurchaseOfferEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in cash_offer_elections (list)
        _items = []
        if self.cash_offer_elections:
            for _item in self.cash_offer_elections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cashOfferElections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lapse_elections (list)
        _items = []
        if self.lapse_elections:
            for _item in self.lapse_elections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lapseElections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tender_offer_elections (list)
        _items = []
        if self.tender_offer_elections:
            for _item in self.tender_offer_elections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tenderOfferElections'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if response_deadline_date (nullable) is None
        # and __fields_set__ contains the field
        if self.response_deadline_date is None and "response_deadline_date" in self.__fields_set__:
            _dict['responseDeadlineDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RepurchaseOfferEvent:
        """Create an instance of RepurchaseOfferEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RepurchaseOfferEvent.parse_obj(obj)

        _obj = RepurchaseOfferEvent.parse_obj({
            "instrument_event_type": obj.get("instrumentEventType"),
            "payment_date": obj.get("paymentDate"),
            "market_deadline_date": obj.get("marketDeadlineDate"),
            "repurchase_quantity": obj.get("repurchaseQuantity"),
            "cash_offer_elections": [CashOfferElection.from_dict(_item) for _item in obj.get("cashOfferElections")] if obj.get("cashOfferElections") is not None else None,
            "lapse_elections": [LapseElection.from_dict(_item) for _item in obj.get("lapseElections")] if obj.get("lapseElections") is not None else None,
            "tender_offer_elections": [TenderOfferElection.from_dict(_item) for _item in obj.get("tenderOfferElections")] if obj.get("tenderOfferElections") is not None else None,
            "proration_rate": obj.get("prorationRate") if obj.get("prorationRate") is not None else 1,
            "response_deadline_date": obj.get("responseDeadlineDate")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
