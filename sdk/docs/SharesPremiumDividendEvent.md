# SharesPremiumDividendEvent

Shares premium dividend (SHPR): a mandatory cash payment to shareholders out of the issuer's share premium  reserve. It is similar to a dividend but is booked as a return of capital: units are unchanged, cost falls by the  cash received and no income is recognised. Mandatory with one cash election, or MandatoryWithChoices for a  currency choice.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Date on which the share premium distribution is announced by the company. Informational. | [optional] 
**cash_elections** | [**List[CashElection]**](CashElection.md) | Possible cash elections for this event, each keyed with a unique identifier. One when Mandatory; two or more when MandatoryWithChoices. | 
**ex_date** | **datetime** | The first business day on which the distribution is not owed to the buying party. The entitlement date and the trade date. | [optional] 
**payment_date** | **datetime** | The date the share premium distribution is paid. The settlement date of the generated transaction. | [optional] 
**record_date** | **datetime** | Date you have to be the holder of record in order to receive the distribution. Informational. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent, SharesPremiumDividendEvent, CashDistributionFromNonEligibleSecuritiesSalesEvent, InflationIndexationEvent. | 
## Example

```python
from lusid.models.shares_premium_dividend_event import SharesPremiumDividendEvent
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
shares_premium_dividend_event_instance = SharesPremiumDividendEvent(announcement_date=announcement_date, cash_elections=cash_elections, ex_date=ex_date, payment_date=payment_date, record_date=record_date, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

