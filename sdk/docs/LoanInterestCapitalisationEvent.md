# LoanInterestCapitalisationEvent

Event to signify that interest accrued against a loan holding is settled in kind: the amount is  capitalised into the loan's balance instead of being paid in cash.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date that the capitalisation is effective. Capitalisation has no cash to settle, so nothing can lag  the accrual it capitalises and this is the ex-date. | [optional] 
**ex_date** | **datetime** | Date that the in-kind accrued interest is calculated up until. | [optional] 
**currency** | **str** | Currency of the capitalised amount. | 
**fraction** | **float** | Fraction of the in-kind accrued on the holding to be capitalised. Must be between 0 and 1, inclusive.  Defaults to 1 if not set. The accrual is reset in full whatever this is: an issuer who elects to  capitalise part of the in-kind leg has still settled the period. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | Election for controlling whether the interest is capitalised automatically or not.  Exactly one election must be provided. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent. | 
## Example

```python
from lusid.models.loan_interest_capitalisation_event import LoanInterestCapitalisationEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
fraction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
loan_interest_capitalisation_event_instance = LoanInterestCapitalisationEvent(payment_date=payment_date, ex_date=ex_date, currency=currency, fraction=fraction, lapse_elections=lapse_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

