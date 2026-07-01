# LiquidationPaymentEvent

A liquidation payment event (LIQU).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The announcement date. Optional; informational only. | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | The cash offer elections for this event. | 
**ex_date** | **datetime** | The ex-date. Optional; informational only — entitlement uses RecordDate. | [optional] 
**is_final** | **bool** | True if this is the final distribution and the position should be closed; false for a partial distribution  where the position is retained and cost basis is reduced by the cash amount. | 
**payment_date** | **datetime** | The date the cash distribution is settled. | [optional] 
**record_date** | **datetime** | The record date used to determine eligible holdings via settled units. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent. | 
## Example

```python
from lusid.models.liquidation_payment_event import LiquidationPaymentEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

announcement_date: Optional[datetime] = # Replace with your value
cash_offer_elections: List[CashOfferElection] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
is_final: StrictBool = # Replace with your value
is_final:StrictBool = True
payment_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
liquidation_payment_event_instance = LiquidationPaymentEvent(announcement_date=announcement_date, cash_offer_elections=cash_offer_elections, ex_date=ex_date, is_final=is_final, payment_date=payment_date, record_date=record_date, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

