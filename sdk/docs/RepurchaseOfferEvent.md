# RepurchaseOfferEvent

Representation of a repurchase offer corporate action.  Represents an offer by the issuer to repurchase its own shares from a shareholder at a given price.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Payment date of the event. | [optional] 
**market_deadline_date** | **datetime** | Date set by the issuer or by an agent of the issuer as the latest date to respond to the offer. Must be before or equal to the PaymentDate. | [optional] 
**repurchase_quantity** | **float** | Quantity of the security to be repurchased. | 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | List of possible CashOfferElections for this event. Only 1 should be provided. | 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | List of possible LapseElections for this event. Only 1 should be provided.  Allows the user to opt out of the offer. | 
**tender_offer_elections** | [**List[TenderOfferElection]**](TenderOfferElection.md) | List of possible TenderOfferElections for this event. Only 1 should be provided. | 
**proration_rate** | **float** | The fraction used to calculate a proportional adjustment for RepurchaseQuantity when a full period is not used.  Defaults to 1 if not set. Must be greater than 0 and less than or equal to 1. | [optional] [default to 1]
**response_deadline_date** | **datetime** | Date set by the account servicer as the latest date to respond to the offer.  Optional. If set, must be before or equal to MarketDeadlineDate.  Defaults to MarketDeadlineDate if not set. | [optional] 
**early_response_deadline** | **datetime** | Optional CTEN early-tender deadline. If set, must be on or before ResponseDeadlineDate.  Used for bond tender offers where early tenders attract a premium. | [optional] 
**min_piece_size** | **float** | Bond-specific minimum instructable face amount. Optional.  Must be strictly positive when set. | [optional] 
**min_increment** | **float** | Bond-specific increment above MinPieceSize. Optional.  When set, MinPieceSize must also be set. Must be strictly positive. | [optional] 
**accrued_interest_per_unit** | **float** | Optional per-unit accrued interest on the accepted face amount, from the last coupon date  up to (but excluding) PaymentDate. Bond-like instruments only. If left empty,  resolves it internally at event time from the bond&#39;s coupon schedule and market data. | [optional] 
**consent_and_tender_elections** | [**List[ConsentAndTenderElection]**](ConsentAndTenderElection.md) | List of possible consent-and-tender elections for this event (CTEN) — tender the holding and grant consent together. | [optional] 
**consent_granted_elections** | [**List[ConsentGrantedElection]**](ConsentGrantedElection.md) | List of possible consent-granted elections for this event (CONY) — vote in favour, optionally attracting a consent fee. | [optional] 
**consent_denied_elections** | [**List[ConsentDeniedElection]**](ConsentDeniedElection.md) | List of possible consent-denied elections for this event (CONN) — vote against the proposal. | [optional] 
**abstain_elections** | [**List[AbstainElection]**](AbstainElection.md) | List of possible abstain elections for this event (ABST) — decline to vote on the consent. | [optional] 
**unknown_proceeds_elections** | [**List[UnknownProceedsElection]**](UnknownProceedsElection.md) | List of possible unknown-proceeds elections for this event (UNKNOWN) — the outturn is not yet known. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent. | 
## Example

```python
from lusid.models.repurchase_offer_event import RepurchaseOfferEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
market_deadline_date: Optional[datetime] = # Replace with your value
repurchase_quantity: Union[StrictFloat, StrictInt] = # Replace with your value
cash_offer_elections: List[CashOfferElection] = # Replace with your value
lapse_elections: List[LapseElection] = # Replace with your value
tender_offer_elections: List[TenderOfferElection] = # Replace with your value
proration_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
response_deadline_date: Optional[datetime] = # Replace with your value
early_response_deadline: Optional[datetime] = # Replace with your value
min_piece_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
min_increment: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
accrued_interest_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
consent_and_tender_elections: Optional[List[ConsentAndTenderElection]] = # Replace with your value
consent_granted_elections: Optional[List[ConsentGrantedElection]] = # Replace with your value
consent_denied_elections: Optional[List[ConsentDeniedElection]] = # Replace with your value
abstain_elections: Optional[List[AbstainElection]] = # Replace with your value
unknown_proceeds_elections: Optional[List[UnknownProceedsElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
repurchase_offer_event_instance = RepurchaseOfferEvent(payment_date=payment_date, market_deadline_date=market_deadline_date, repurchase_quantity=repurchase_quantity, cash_offer_elections=cash_offer_elections, lapse_elections=lapse_elections, tender_offer_elections=tender_offer_elections, proration_rate=proration_rate, response_deadline_date=response_deadline_date, early_response_deadline=early_response_deadline, min_piece_size=min_piece_size, min_increment=min_increment, accrued_interest_per_unit=accrued_interest_per_unit, consent_and_tender_elections=consent_and_tender_elections, consent_granted_elections=consent_granted_elections, consent_denied_elections=consent_denied_elections, abstain_elections=abstain_elections, unknown_proceeds_elections=unknown_proceeds_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

