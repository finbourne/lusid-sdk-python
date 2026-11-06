# CashDistributionFromNonEligibleSecuritiesSalesEvent

Cash distribution from non-eligible securities sales (DRCA). An agent sells the securities that some holders  cannot receive (for example the underlying of a depositary receipt programme) and pays those holders the cash  proceeds. The holder receives one per-unit cash amount on the eligible balance; units and cost do not change.  Mandatory participation only, with exactly one CashElection in one currency at an exchange rate of 1.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Date on which the distribution was announced. Optional and informational. | [optional] 
**cash_elections** | [**List[CashElection]**](CashElection.md) | Exactly one CashElection, with isDeclared, isDefault and isChosen all true, carrying the net cash per unit that settles to the holder after any agent fee. No currency choice, rate breakdown or election-level payment date. | 
**ex_date** | **datetime** | The first business day on which the distribution is not owed to the buying party. The entitlement date and the transaction date. | [optional] 
**payment_date** | **datetime** | The date the cash proceeds are paid to the holder. The settlement date of the generated transaction. | [optional] 
**record_date** | **datetime** | The date positions are struck for entitlement. Required: AMI-SeCo Annex 2 requires a record date for DRCA. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent, SharesPremiumDividendEvent, CashDistributionFromNonEligibleSecuritiesSalesEvent, InflationIndexationEvent. | 
## Example

```python
from lusid.models.cash_distribution_from_non_eligible_securities_sales_event import CashDistributionFromNonEligibleSecuritiesSalesEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

announcement_date: Optional[datetime] = # Replace with your value
cash_elections: List[CashElection] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
cash_distribution_from_non_eligible_securities_sales_event_instance = CashDistributionFromNonEligibleSecuritiesSalesEvent(announcement_date=announcement_date, cash_elections=cash_elections, ex_date=ex_date, payment_date=payment_date, record_date=record_date, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

