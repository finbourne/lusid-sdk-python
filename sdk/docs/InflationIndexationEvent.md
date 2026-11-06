# InflationIndexationEvent

The day-on-day change in the indexed face of an inflation-linked bond, as its inflation index ratio moves  from one day to the next. A memo event: downstream it books a transaction whose units carry the day's indexed-face  change (the principal uplift) and whose cash is zero; nothing moves.  Mandatory participation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The bond&#39;s domestic currency. | 
**event_date** | **datetime** | The calendar day on which the new index ratio applies. On an event LUSID generates it carries the bond&#39;s  local offset, so its date part is the bond&#39;s local calendar day; it is returned as generated and not  normalised to UTC. An upserted event may give it with any offset; it is normalised to UTC when stored. | [optional] 
**index_ratio_after** | **float** | The bond&#39;s un-floored inflation index ratio on the event date. | 
**index_ratio_before** | **float** | The bond&#39;s un-floored inflation index ratio on the day before the event date. | 
**indexed_face_change_per_unit** | **float** | The day&#39;s change in indexed face per unit: the un-indexed face per unit multiplied by  (index ratio after minus index ratio before). | 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent, SharesPremiumDividendEvent, CashDistributionFromNonEligibleSecuritiesSalesEvent, InflationIndexationEvent. | 
## Example

```python
from lusid.models.inflation_indexation_event import InflationIndexationEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

currency: StrictStr = "example_currency"
event_date: Optional[datetime] = # Replace with your value
index_ratio_after: Union[StrictFloat, StrictInt] = # Replace with your value
index_ratio_before: Union[StrictFloat, StrictInt] = # Replace with your value
indexed_face_change_per_unit: Union[StrictFloat, StrictInt] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
inflation_indexation_event_instance = InflationIndexationEvent(currency=currency, event_date=event_date, index_ratio_after=index_ratio_after, index_ratio_before=index_ratio_before, indexed_face_change_per_unit=indexed_face_change_per_unit, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

