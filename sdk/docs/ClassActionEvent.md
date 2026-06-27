# ClassActionEvent

Class Action Event (CLSA) — a voluntary corporate action under which security holders  receive cash compensation from a court-approved settlement fund following litigation  against an issuer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date on which the settlement distribution is paid to the holder. | [optional] 
**filing_deadline** | **datetime** | Court-set deadline for submitting a proof of claim. | [optional] 
**class_period_start** | **datetime** | Lower bound of the eligibility window (inclusive). | [optional] 
**class_period_end** | **datetime** | Upper bound of the eligibility window (inclusive). | [optional] 
**ex_date** | **datetime** | Date from which the security trades without the settlement right.  Null for most class actions where no ex date is defined. | [optional] 
**record_date** | **datetime** | Date at which positions are struck for notification scope. Informational only. | [optional] 
**announcement_date** | **datetime** | Settlement public-announcement or court-approval date. | [optional] 
**case_reference** | **str** | Lawsuit or settlement-fund identifier (court case number, fund name). Audit-only. | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | Cash offer elections for this event. Exactly one entry carrying the per-share  settlement amount as CashOfferPrice and settlement currency as CashOfferCurrency. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | Lapse elections for this event. Exactly one entry (NOAC) with IsDefault &#x3D; true. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent. | 
## Example

```python
from lusid.models.class_action_event import ClassActionEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
filing_deadline: Optional[datetime] = # Replace with your value
class_period_start: Optional[datetime] = # Replace with your value
class_period_end: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
case_reference: Optional[StrictStr] = "example_case_reference"
cash_offer_elections: Optional[List[CashOfferElection]] = # Replace with your value
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
class_action_event_instance = ClassActionEvent(payment_date=payment_date, filing_deadline=filing_deadline, class_period_start=class_period_start, class_period_end=class_period_end, ex_date=ex_date, record_date=record_date, announcement_date=announcement_date, case_reference=case_reference, cash_offer_elections=cash_offer_elections, lapse_elections=lapse_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

