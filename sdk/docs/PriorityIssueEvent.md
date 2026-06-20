# PriorityIssueEvent

Priority Issue Event (PRIO) — a voluntary corporate action in which an issuer offers existing  security holders preferential rights to subscribe for new securities at a defined subscription  price before the offer is opened to the wider market. Holders may subscribe up to a basic  entitlement (SECU) and, where offered, apply for additional securities beyond the basic  entitlement (OVER, subject to proration). No instruction (NOAC) results in no transaction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Date on which the priority issue was announced. Optional, informational. | [optional] 
**ex_date** | **datetime** | First business day on which the security trades without the entitlement. Optional.  When not supplied, transaction-template generation falls back to RecordDate | [optional] 
**record_date** | **datetime** | The entitlement determination date — holders of record on this date are eligible to subscribe. | [optional] 
**response_deadline** | **datetime** | The account-servicer instruction deadline. Must be less than or equal to MarketDeadline. | [optional] 
**market_deadline** | **datetime** | The issuer-agent deadline. | [optional] 
**payment_date** | **datetime** | Date on which cash is debited and the new securities are credited. | [optional] 
**security_settlement_date** | **datetime** | Date the security leg settles when it differs from the cash leg. Optional.  When not supplied, transaction-template generation falls back to PaymentDate | [optional] 
**subscription_price** | **float** | The subscription price per new unit. Applies to both SECU and OVER subscriptions.  Must be greater than zero. | [optional] 
**subscription_currency** | **str** | Currency of the SubscriptionPrice. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | [optional] 
**proration_rate** | **float** | The proration rate applied to OVER subscriptions when the offer is oversubscribed.  Treated as 1 (full allocation) when not supplied. Must be greater than 0 and less than  or equal to 1. SECU basic entitlement is never prorated. | [optional] 
**fractional_units_cash_price** | **float** | Price per fractional unit used to compute cash-in-lieu for fractional entitlement remainders.  When not supplied, fractional residuals are discarded with no cash-in-lieu.  Forms an optional pair with FractionalUnitsCashCurrency — both must be supplied together. | [optional] 
**fractional_units_cash_currency** | **str** | Currency of FractionalUnitsCashPrice. Required if and only if FractionalUnitsCashPrice is supplied. | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) | Security offer elections — exactly one entry keyed &#39;SECU&#39; (basic entitlement) and an optional  entry keyed &#39;OVER&#39; (over-subscription) when the issuer offers the over-subscription facility. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | Lapse elections — exactly one entry keyed &#39;NOAC&#39;, recording the holder&#39;s explicit no-action election. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent. | 
## Example

```python
from lusid.models.priority_issue_event import PriorityIssueEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

announcement_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
response_deadline: Optional[datetime] = # Replace with your value
market_deadline: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
security_settlement_date: Optional[datetime] = # Replace with your value
subscription_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
subscription_currency: Optional[StrictStr] = "example_subscription_currency"
new_instrument: Optional[NewInstrument] = # Replace with your value
proration_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
security_offer_elections: Optional[List[SecurityOfferElection]] = # Replace with your value
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
priority_issue_event_instance = PriorityIssueEvent(announcement_date=announcement_date, ex_date=ex_date, record_date=record_date, response_deadline=response_deadline, market_deadline=market_deadline, payment_date=payment_date, security_settlement_date=security_settlement_date, subscription_price=subscription_price, subscription_currency=subscription_currency, new_instrument=new_instrument, proration_rate=proration_rate, fractional_units_cash_price=fractional_units_cash_price, fractional_units_cash_currency=fractional_units_cash_currency, security_offer_elections=security_offer_elections, lapse_elections=lapse_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

