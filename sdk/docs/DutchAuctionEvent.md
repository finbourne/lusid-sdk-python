# DutchAuctionEvent

Dutch Auction Event (DTCH) — a voluntary corporate action with price-discovery, proration,  and per-holder bid audit. Tri-modal: CASH (uniform clearing-price cash buyback via  TenderOfferElection), SECU (clean security-for-security exchange via SecurityOfferElection),  or CASE (security exchange with signed per-unit cash settlement via CashAndSecurityOfferElection).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Settlement date for both the security and cash legs of the auction. | [optional] 
**market_deadline_date** | **datetime** | Issuer or acquirer instruction deadline. | [optional] 
**currency** | **str** | Event settlement currency (ISO 4217). | 
**tender_offer_elections** | [**List[TenderOfferElection]**](TenderOfferElection.md) | List of possible TenderOfferElections for this event. Populated on the CASH path (Count &#x3D;&#x3D; 1);  empty on the SECU and CASE paths. | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) | List of possible SecurityOfferElections for this event. Populated on the SECU path (Count &#x3D;&#x3D; 1);  empty on the CASH and CASE paths. | [optional] 
**cash_and_security_offer_elections** | [**List[CashAndSecurityOfferElection]**](CashAndSecurityOfferElection.md) | List of possible CashAndSecurityOfferElections for this event. Populated on the CASE path  (Count &#x3D;&#x3D; 1); empty on the CASH and SECU paths. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | List of possible LapseElections for this event. Required on all three paths (Count &#x3D;&#x3D; 1).  Allows the holder to opt out of the offer (NOAC). | [optional] 
**response_deadline_date** | **datetime** | Account-servicer response deadline. Defaults to MarketDeadlineDate when not supplied.  When provided, must be on or before MarketDeadlineDate. | [optional] 
**early_response_deadline** | **datetime** | Early-participation deadline. When provided, must be on or before ResponseDeadlineDate. | [optional] 
**ex_date** | **datetime** | The ex date of the event. Optional; carried for cross-event consistency. | [optional] 
**record_date** | **datetime** | The record date of the event. Optional and not required by AMI-SeCo for DTCH  (the event is instruction-driven via QINS, not record-date-driven). | [optional] 
**announcement_date** | **datetime** | Public announcement date of the auction. Optional. | [optional] 
**target_quantity** | **float** | Total quantity of securities sought by the issuer or acquirer. Optional. | [optional] 
**proration_rate** | **float** | Proportional adjustment applied to the security and cash legs on all paths.  Must be in (0, 1]. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | [optional] 
**fractional_units_cash_price** | **float** | Cash-in-lieu price per fractional unit on the SECU and CASE paths.  Null indicates round-down disposition of fractional remainders.  Distinct from the CASE path&#39;s main cash settlement (which lives on CashAndSecurityOfferElection). | [optional] 
**fractional_units_cash_currency** | **str** | Currency of the cash-in-lieu paid on fractional remainders on the SECU and CASE paths.  Required when FractionalUnitsCashPrice is non-null. | [optional] 
**bid_price** | **float** | Per-holder bid price submitted at instruction time. Audit-only; no calculation impact. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent. | 
## Example

```python
from lusid.models.dutch_auction_event import DutchAuctionEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
market_deadline_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
tender_offer_elections: Optional[List[TenderOfferElection]] = # Replace with your value
security_offer_elections: Optional[List[SecurityOfferElection]] = # Replace with your value
cash_and_security_offer_elections: Optional[List[CashAndSecurityOfferElection]] = # Replace with your value
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
response_deadline_date: Optional[datetime] = # Replace with your value
early_response_deadline: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
target_quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
proration_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
new_instrument: Optional[NewInstrument] = # Replace with your value
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
bid_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
dutch_auction_event_instance = DutchAuctionEvent(payment_date=payment_date, market_deadline_date=market_deadline_date, currency=currency, tender_offer_elections=tender_offer_elections, security_offer_elections=security_offer_elections, cash_and_security_offer_elections=cash_and_security_offer_elections, lapse_elections=lapse_elections, response_deadline_date=response_deadline_date, early_response_deadline=early_response_deadline, ex_date=ex_date, record_date=record_date, announcement_date=announcement_date, target_quantity=target_quantity, proration_rate=proration_rate, new_instrument=new_instrument, fractional_units_cash_price=fractional_units_cash_price, fractional_units_cash_currency=fractional_units_cash_currency, bid_price=bid_price, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

