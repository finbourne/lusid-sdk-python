# BonusIssueEvent

Representation of a Bonus Issue corporate action.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The date the Bonus Issue is announced. | [optional] 
**ex_date** | **datetime** | The ex-date of the Bonus Issue. | [optional] 
**record_date** | **datetime** | The record date of the Bonus Issue. | [optional] 
**payment_date** | **datetime** | The date the Bonus Issue is executed. | [optional] 
**fractional_units_cash_price** | **float** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**fractional_units_cash_currency** | **str** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) | Possible SecurityElections for this Bonus Issue event, if any. | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | Possible CashOfferElections for this Bonus Issue event, if any. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | Possible LapseElections for this Bonus Issue event, if any. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent | 
## Example

```python
from lusid.models.bonus_issue_event import BonusIssueEvent
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from datetime import datetime
announcement_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
security_offer_elections: Optional[conlist(SecurityOfferElection)] = # Replace with your value
cash_offer_elections: Optional[conlist(CashOfferElection)] = # Replace with your value
lapse_elections: Optional[conlist(LapseElection)] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
bonus_issue_event_instance = BonusIssueEvent(announcement_date=announcement_date, ex_date=ex_date, record_date=record_date, payment_date=payment_date, fractional_units_cash_price=fractional_units_cash_price, fractional_units_cash_currency=fractional_units_cash_currency, security_offer_elections=security_offer_elections, cash_offer_elections=cash_offer_elections, lapse_elections=lapse_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

