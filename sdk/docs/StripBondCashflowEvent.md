# StripBondCashflowEvent

A StripBond's receipt of one (payment date, ex date) pair of its parent's flows: the coupons of an  interest-only strip, the principal paydowns of a principal-only one. The cash per unit of original face is the  parent's amount over its initial notional. The booking splits that cash into income and return of capital by  the strip's effective yield. The three outputs the split needs, effectiveYield, accountingChoice and isFinal,  are filled from the recipe's StripBondModelOptions and the market when omitted, and a supplied value wins for  each. A posted event under the generated id replaces the generated one.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The parent flow&#39;s ex-date, the record-date boundary: a lot settled on or after it is not entitled. Required. | [optional] 
**payment_date** | **datetime** | The payment date. Required. | [optional] 
**currency** | **str** | The parent&#39;s payment currency. Required. | 
**cash_flow_per_unit** | **float** | The strip&#39;s cash per unit of original face on this date: the summed parent amount divided by the parent&#39;s  initial notional. Required. | 
**payments_per_year** | **int** | The parent&#39;s payments per year, 12 for a monthly parent. The nominal annual yield over this is the  periodic yield a receipt is split on. Required. | 
**effective_yield** | **float** | The nominal annual yield applied, as a decimal (0.23646524 for 23.646524%). Optional: filled from the  accounting choice when omitted, 0 under CostRecovery, the strip&#39;s EffectiveYield quote at the ex-date under  QuotedYield, left empty under CashAsReceived, which uses no yield. A supplied value wins. | [optional] 
**accounting_choice** | **str** | The accounting choice the split uses. Optional: filled from the recipe&#39;s StripBondModelOptions when omitted,  CostRecovery when there are none. A supplied value wins.                Supported string (enumeration) values are: [CostRecovery, QuotedYield, CashAsReceived]. Available values: CostRecovery, QuotedYield, CashAsReceived. | [optional] 
**is_final** | **bool** | Whether the parent&#39;s notional after this payment is zero, so this is the strip&#39;s last payment and the  position closes. Optional: filled from the parent&#39;s populated pool factor at the payment date when omitted,  or its maturity for a parent without one. A supplied value wins. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent. | 
## Example

```python
from lusid.models.strip_bond_cashflow_event import StripBondCashflowEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ex_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
cash_flow_per_unit: Union[StrictFloat, StrictInt] = # Replace with your value
payments_per_year: StrictInt = # Replace with your value
payments_per_year: StrictInt = 42
effective_yield: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
accounting_choice: Optional[StrictStr] = "example_accounting_choice"
is_final: Optional[StrictBool] = # Replace with your value
is_final:Optional[StrictBool] = None
instrument_event_type: StrictStr = "example_instrument_event_type"
strip_bond_cashflow_event_instance = StripBondCashflowEvent(ex_date=ex_date, payment_date=payment_date, currency=currency, cash_flow_per_unit=cash_flow_per_unit, payments_per_year=payments_per_year, effective_yield=effective_yield, accounting_choice=accounting_choice, is_final=is_final, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

