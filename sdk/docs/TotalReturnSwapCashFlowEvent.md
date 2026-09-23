# TotalReturnSwapCashFlowEvent

A scheduled exchange of a TotalReturnSwap: a funding-leg coupon or notional exchange, an asset income or  principal passed through on the asset leg, or a price-return reset of the asset leg. Component says  which. The amount is per unit of the swap as its cash flows are booked, signed negative when paid; it is  absent until the market data determining it has been published.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The date the holding must be held on to be entitled to the flow. Required. | [optional] 
**payment_date** | **datetime** | The date the flow pays. Required. | [optional] 
**currency** | **str** | The currency the flow pays in. Required. | 
**component** | **str** | Which exchange of the swap the flow settles. Required.                Supported string (enumeration) values are: [FundingPayment, FundingNotional, AssetIncome, AssetPrincipal, PriceReturn]. | 
**flow_type** | **str** | The type of the underlying cash flow the event settles. A component can gather several flow types  paying on one date (an asset-backed bond&#39;s coupon, interest deferral and interest shortfall are all  asset income), so the flow type is what tells them apart. Required.                Supported string (enumeration) values are: [Coupon, Notional, Premium, Principal, Protection, Cash, Dividend, Interest, PrincipalWriteOff, InterestDeferred, InterestShortfall, MarkToMarket, InterestInKind]. | 
**leg_identifier** | **str** | The leg the flow belongs to. Required.                Supported string (enumeration) values are: [AssetLeg, FundingLeg]. | 
**pay_receive** | **str** | Whether the flow is paid or received from the holder&#39;s perspective. The amount is already signed  accordingly; this attributes an undetermined flow to its side. Required.                Supported string (enumeration) values are: [Pay, Receive]. | 
**cash_flow_per_unit** | **float** | The signed amount per unit of the swap held on the ex date, negative when paid. Optional — absent  until determinable: a price-return reset needs its reset quotes, a floating funding payment its fixing. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent. | 
## Example

```python
from lusid.models.total_return_swap_cash_flow_event import TotalReturnSwapCashFlowEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ex_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
component: StrictStr = "example_component"
flow_type: StrictStr = "example_flow_type"
leg_identifier: StrictStr = "example_leg_identifier"
pay_receive: StrictStr = "example_pay_receive"
cash_flow_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
total_return_swap_cash_flow_event_instance = TotalReturnSwapCashFlowEvent(ex_date=ex_date, payment_date=payment_date, currency=currency, component=component, flow_type=flow_type, leg_identifier=leg_identifier, pay_receive=pay_receive, cash_flow_per_unit=cash_flow_per_unit, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

