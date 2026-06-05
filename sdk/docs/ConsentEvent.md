# ConsentEvent

Consent Event (CONS) — a voluntary corporate action where an issuer seeks approval  from security holders to amend the terms of an outstanding instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_type** | **str** | The type of consent solicitation.                Supported string (enumeration) values are: [ChangeInTerms, DueAndPayable]. Available values: ChangeInTerms, DueAndPayable. | 
**record_date** | **datetime** | The entitlement determination date. | [optional] 
**response_deadline** | **datetime** | The last date to submit instructions. | [optional] 
**market_deadline** | **datetime** | The issuer-set outer deadline. Must be greater than or equal to ResponseDeadline. | [optional] 
**early_response_deadline** | **datetime** | Deadline for early consent. Required when a CONY-early CashOfferElection is offered.  Must be earlier than ResponseDeadline. | [optional] 
**payment_date** | **datetime** | Date on which the consent fee is paid. Required when any CashOfferElection is offered. | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | List of possible cash offer elections for this event. Each tier (CONY-standard, CONY-early)  is modelled as a separate entry; the election carries the per-unit fee rate and currency. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | List of possible lapse elections for this event (NOAC, CONN, ABST). | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent. | 
## Example

```python
from lusid.models.consent_event import ConsentEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

consent_type: StrictStr = "example_consent_type"
record_date: Optional[datetime] = # Replace with your value
response_deadline: Optional[datetime] = # Replace with your value
market_deadline: Optional[datetime] = # Replace with your value
early_response_deadline: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
cash_offer_elections: Optional[List[CashOfferElection]] = # Replace with your value
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
consent_event_instance = ConsentEvent(consent_type=consent_type, record_date=record_date, response_deadline=response_deadline, market_deadline=market_deadline, early_response_deadline=early_response_deadline, payment_date=payment_date, cash_offer_elections=cash_offer_elections, lapse_elections=lapse_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

