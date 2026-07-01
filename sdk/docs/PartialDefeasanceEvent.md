# PartialDefeasanceEvent

Partial Defeasance event (PDEF). A mandatory notification that a bond issuer has escrow-funded  (defeased) a portion of an outstanding issue. No cash flows to holders at this event; the position  is marked pre-refunded and its effective maturity is updated to the future call date carried in  ActualPayDate. The actual cash and position retirement arrive later via a separate  mandatory call event. Supports a Partial Pre-Refunding variant (PPRE).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refunded_fraction** | **float** | The issue-level fraction allocated to the refunded (pre-refunded / escrowed) portion. Strictly  in the half-open interval (0, 1]; the non-refunded fraction is the derived complement. This is a  required field. | 
**effective_date** | **datetime** | The date the defeasance status takes effect on the position. This is a required field. | [optional] 
**actual_pay_date** | **datetime** | The future call date when the bond will actually be retired, used to update the position&#39;s  effective maturity in analytics. Must be on or after EffectiveDate. This is a  required field. | [optional] 
**refunded_instrument** | [**NewInstrument**](NewInstrument.md) |  | [optional] 
**new_securities_indicator** | **str** | Optional audit field preserving the wire-side codeword used for the refunded portion.  Supported string (enumeration) values are: [REFU, DEFE]. Both encodings carry identical semantics. Available values: REFU, DEFE. | [optional] 
**additional_business_process** | **str** | Optional variant indicator. Supported string (enumeration) values are: [PPRE]. Absence (null)  encodes the default Partial Defeasance variant. Available values: PPRE. | [optional] 
**lottery_date** | **datetime** | Optional. The wire&#39;s lottery date; null when the wire carried a sentinel value. | [optional] 
**publication_date** | **datetime** | Optional informational date identifying when the defeasance was publicly noticed. | [optional] 
**record_date** | **datetime** | Optional. The wire&#39;s record date; typically null for a notification event with no distribution. | [optional] 
**announcement_date** | **datetime** | Optional informational announcement date; null when not provided. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent. | 
## Example

```python
from lusid.models.partial_defeasance_event import PartialDefeasanceEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

refunded_fraction: Union[StrictFloat, StrictInt] = # Replace with your value
effective_date: Optional[datetime] = # Replace with your value
actual_pay_date: Optional[datetime] = # Replace with your value
refunded_instrument: Optional[NewInstrument] = # Replace with your value
new_securities_indicator: Optional[StrictStr] = "example_new_securities_indicator"
additional_business_process: Optional[StrictStr] = "example_additional_business_process"
lottery_date: Optional[datetime] = # Replace with your value
publication_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
partial_defeasance_event_instance = PartialDefeasanceEvent(refunded_fraction=refunded_fraction, effective_date=effective_date, actual_pay_date=actual_pay_date, refunded_instrument=refunded_instrument, new_securities_indicator=new_securities_indicator, additional_business_process=additional_business_process, lottery_date=lottery_date, publication_date=publication_date, record_date=record_date, announcement_date=announcement_date, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

