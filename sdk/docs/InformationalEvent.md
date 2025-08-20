# InformationalEvent

A generic event derived from the economic definition of an instrument. This should be considered purely informational; any data provided by this event is not guaranteed to be processable by LUSID.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | What type of internal event does this represent; reset, exercise, amortisation etc. | [readonly] 
**anchor_date** | **datetime** | In the case of a point event, the single date on which the event occurs. In the case of an event which is spread over a window, e.g. a barrier or American option, the start of that window. | 
**event_window_end** | **datetime** | In the case of a point event this is identical to the anchor date. In the case of an event that is spread over a window, this is the end of that window. | [optional] [readonly] 
**diagnostics** | [**ResultValueDictionary**](ResultValueDictionary.md) |  | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent | 
## Example

```python
from lusid.models.informational_event import InformationalEvent
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictStr, constr, validator
from datetime import datetime
event_type: StrictStr = "example_event_type"
anchor_date: datetime = # Replace with your value
event_window_end: Optional[datetime] = # Replace with your value
diagnostics: Optional[ResultValueDictionary] = None
instrument_event_type: StrictStr = "example_instrument_event_type"
informational_event_instance = InformationalEvent(event_type=event_type, anchor_date=anchor_date, event_window_end=event_window_end, diagnostics=diagnostics, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

