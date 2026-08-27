# CommodityCalendarSwapCashFlowEvent

Cash settlement of one calendar-average period of a CommodityCalendarSwap. One event fires per period  end date defined by the swap's schedule, including the final period; PeriodNumber identifies which.  The cash flow per unit is the pre-netted settlement price (the calendar average of the observed  commodity price minus the strike) supplied externally via the quote store — LUSID computes neither the  average nor the netting. A negative value is valid and means the period settled out of the money.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_end_date** | **datetime** | The end date of the settling period, derived from the swap&#39;s schedule. The period settles against  the calendar average of the observed commodity price up to this date. Required, and the effective  date of the event. | [optional] 
**payment_date** | **datetime** | The settlement date of the period, already adjusted for the schedule&#39;s business day convention,  payment calendars and coupon lag. Required. This is when the cash moves; the event itself is  effective at PeriodEndDate. | [optional] 
**currency** | **str** | The currency the period settles in, taken from the schedule&#39;s payment currency. Required. | 
**period_number** | **int** | The sequential number of the settling period, with the first period being 1 and the final period  being the total number of periods in the schedule. Required. | 
**quantity_per_period** | **float** | The notional commodity quantity referenced by the period, and the number of units by which the  holding is reduced when the period settles. Required. | 
**ex_date** | **datetime** | The ex-dividend date of the cash flow. Always equal to PeriodEndDate, since entitlement is  determined by the holding on the period end date. Required. | [optional] 
**cash_flow_per_unit** | **float** | The pre-netted settlement amount per unit for the period (the calendar average of the observed  commodity price minus the strike), supplied externally via the quote store. Optional — absent until  the settlement price has been resolved. Negative when the period settled out of the money. | [optional] 
**cash_flow_amount** | **float** | The settlement amount for the period, calculated as CashFlowPerUnit multiplied by  QuantityPerPeriod. Optional — absent until the settlement price has been resolved. Carries the  sign of CashFlowPerUnit. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent. | 
## Example

```python
from lusid.models.commodity_calendar_swap_cash_flow_event import CommodityCalendarSwapCashFlowEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

period_end_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
period_number: StrictInt = # Replace with your value
period_number: StrictInt = 42
quantity_per_period: Union[StrictFloat, StrictInt] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
cash_flow_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cash_flow_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
commodity_calendar_swap_cash_flow_event_instance = CommodityCalendarSwapCashFlowEvent(period_end_date=period_end_date, payment_date=payment_date, currency=currency, period_number=period_number, quantity_per_period=quantity_per_period, ex_date=ex_date, cash_flow_per_unit=cash_flow_per_unit, cash_flow_amount=cash_flow_amount, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

