# TenderEvent

Tender Event (TEND).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The date the tender is announced. | [optional] 
**ex_date** | **datetime** | The ex date (entitlement date) of the event. | [optional] 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | [optional] 
**payment_date** | **datetime** | The payment date of the event. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**fractional_units_cash_price** | **float** | The cash price paid in lieu of fractionalUnits. | [optional] 
**fractional_units_cash_currency** | **str** | The currency of the cash paid in lieu of fractionalUnits. | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) | List of possible SecurityOfferElections for this event. | [optional] 
**cash_and_security_offer_elections** | [**List[CashAndSecurityOfferElection]**](CashAndSecurityOfferElection.md) | List of possible CashAndSecurityOfferElections for this event. | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | List of possible CashOfferElections for this event. | [optional] 
**offer_type** | **str** | Informational ISO 20022 OfferTp indicator (e.g. \&quot;ACPR\&quot;). Optional. No calculation impact. | [optional] 
**accrued_interest_per_unit** | **float** | Optional per-unit accrued interest on the tendered face, from the last coupon date up to  (but excluding) PaymentDate. Bond instrument types only. If left empty, analytics-core  resolves it at event time from the bond&#39;s coupon schedule and market data. | [optional] 
**min_piece_size** | **float** | Bond-specific minimum instructable face amount. Optional. Must be strictly positive when set. | [optional] 
**min_increment** | **float** | Bond-specific increment above MinPieceSize. Optional. When set, MinPieceSize must also be set.  Must be strictly positive. | [optional] 
**proration_rate** | **float** | Proration applied when the offer is oversubscribed. Defaults to 1 if not set.  Must be greater than 0 and less than or equal to 1. | [optional] [default to 1]
**response_deadline_date** | **datetime** | Account-servicer SLA deadline for holder instruction. Optional at the DTO layer;  required under Voluntary participation on bond instrument types. | [optional] 
**market_deadline_date** | **datetime** | Offeror&#39;s-agent deadline for holder instruction. Optional at the DTO layer;  required under Voluntary participation on bond instrument types. | [optional] 
**early_response_deadline** | **datetime** | Optional early-tender deadline. When set, must be on or before ResponseDeadlineDate. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent. | 
## Example

```python
from lusid.models.tender_event import TenderEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

announcement_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
new_instrument: NewInstrument = # Replace with your value
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
security_offer_elections: Optional[List[SecurityOfferElection]] = # Replace with your value
cash_and_security_offer_elections: Optional[List[CashAndSecurityOfferElection]] = # Replace with your value
cash_offer_elections: Optional[List[CashOfferElection]] = # Replace with your value
offer_type: Optional[StrictStr] = "example_offer_type"
accrued_interest_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
min_piece_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
min_increment: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
proration_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
response_deadline_date: Optional[datetime] = # Replace with your value
market_deadline_date: Optional[datetime] = # Replace with your value
early_response_deadline: Optional[datetime] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
tender_event_instance = TenderEvent(announcement_date=announcement_date, ex_date=ex_date, record_date=record_date, payment_date=payment_date, new_instrument=new_instrument, fractional_units_cash_price=fractional_units_cash_price, fractional_units_cash_currency=fractional_units_cash_currency, security_offer_elections=security_offer_elections, cash_and_security_offer_elections=cash_and_security_offer_elections, cash_offer_elections=cash_offer_elections, offer_type=offer_type, accrued_interest_per_unit=accrued_interest_per_unit, min_piece_size=min_piece_size, min_increment=min_increment, proration_rate=proration_rate, response_deadline_date=response_deadline_date, market_deadline_date=market_deadline_date, early_response_deadline=early_response_deadline, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

