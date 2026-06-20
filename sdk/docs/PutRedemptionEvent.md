# PutRedemptionEvent

Put Redemption (BPUT) — early redemption of a bond at the holder's election under an  indenture-defined put option. Supports both Voluntary (the AMI-SeCo canonical shape) and  Mandatory (a deliberate market extension beyond SCoRE) participation on Bond, ComplexBond,  and InflationLinkedBond instruments. Cloned from RepurchaseOfferEvent (BIDS) and narrowed  to debt with a fixed event-level OfferPrice instead of a per-election holder-bid price.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Settlement date for the cash + security legs of the put redemption. | [optional] 
**offer_price** | **float** | Put price per unit of face value (AMI-SeCo OFFR). Per-100 PRCT semantics —  &#x60;OfferPrice &#x3D; 100.00&#x60; means par; &#x60;97.50&#x60; means 97.5% of par. Must be strictly positive. | 
**currency** | **str** | Settlement currency of the cash leg (ISO 4217 3-letter code). | 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | List of possible CashOfferElections. Exactly one entry per event in both Mandatory and Voluntary paths. | 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | List of possible LapseElections. Exactly one entry for Voluntary (NOAC default). Empty for Mandatory. | 
**market_deadline_date** | **datetime** | Issuer / agent deadline for holder instructions. Required for Voluntary participation;  optional for Mandatory (no holder-deadline concept). | [optional] 
**response_deadline_date** | **datetime** | Account-servicer deadline. Defaults to MarketDeadlineDate when omitted.  If set, must be on or before MarketDeadlineDate. | [optional] 
**early_response_deadline** | **datetime** | Early-participation deadline. Rare on BPUT; carried for cross-event consistency.  If set, must be on or before ResponseDeadlineDate. | [optional] 
**ex_date** | **datetime** | AMI-SeCo §4.6 does not list this for BPUT; carried for cross-event consistency.  If set, must be on or before MarketDeadlineDate. | [optional] 
**announcement_date** | **datetime** | Public announcement date. If set, must be on or before ExDate. | [optional] 
**accrued_interest_per_unit** | **float** | Per-unit accrued interest. Optional — loader / post-processor derives from the bond&#39;s coupon  schedule and day-count when not supplied. EconomicallyComplete enforces non-null for  accrual-bearing instruments via InstrumentTypeAccruesInterest. | [optional] 
**proration_rate** | **float** | Issuer-side aggregate proration cap (AMI-SeCo PROR). Default 1.0; range (0, 1]. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent. | 
## Example

```python
from lusid.models.put_redemption_event import PutRedemptionEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
offer_price: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
cash_offer_elections: List[CashOfferElection] = # Replace with your value
lapse_elections: List[LapseElection] = # Replace with your value
market_deadline_date: Optional[datetime] = # Replace with your value
response_deadline_date: Optional[datetime] = # Replace with your value
early_response_deadline: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
accrued_interest_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
proration_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
put_redemption_event_instance = PutRedemptionEvent(payment_date=payment_date, offer_price=offer_price, currency=currency, cash_offer_elections=cash_offer_elections, lapse_elections=lapse_elections, market_deadline_date=market_deadline_date, response_deadline_date=response_deadline_date, early_response_deadline=early_response_deadline, ex_date=ex_date, announcement_date=announcement_date, accrued_interest_per_unit=accrued_interest_per_unit, proration_rate=proration_rate, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

