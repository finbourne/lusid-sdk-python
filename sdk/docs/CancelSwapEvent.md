# CancelSwapEvent

A cancel opportunity on a cancellable InterestRateSwap, generated once per date in the swap's cancel  schedule. The holder submits the SubscribeElection by the NoticeDueDate to cancel  the swap, and the opportunity lapses if no election is made. When the swap is cancelled, the current  period's coupon still settles and the position then closes at zero cost and proceeds.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_date** | **datetime** | The date on which the swap terminates if cancellation is elected. Always a date from the swap&#39;s cancel  schedule. | [optional] 
**notice_due_date** | **datetime** | The date by which the election must be made, else the cancel opportunity lapses. Derived from the  CancelDate and the swap&#39;s notice convention. Must be &lt;&#x3D; CancelDate. | [optional] 
**subscribe_elections** | [**List[SubscribeElection]**](SubscribeElection.md) | The elections available on this cancel opportunity: exactly one SubscribeElection, keyed &#39;Cancel&#39;.  A chosen election cancels the swap. No chosen election means the opportunity lapsed and the swap  continues unchanged. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent. | 
## Example

```python
from lusid.models.cancel_swap_event import CancelSwapEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cancel_date: Optional[datetime] = # Replace with your value
notice_due_date: Optional[datetime] = # Replace with your value
subscribe_elections: Optional[List[SubscribeElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
cancel_swap_event_instance = CancelSwapEvent(cancel_date=cancel_date, notice_due_date=notice_due_date, subscribe_elections=subscribe_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

