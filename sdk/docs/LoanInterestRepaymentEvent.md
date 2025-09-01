# LoanInterestRepaymentEvent

Event to signify the repayment of interest accrued against a loan holding.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date that the interest is due to be paid. | [optional] 
**ex_date** | **datetime** | Date that the accrued interest is calculated up until. | [optional] 
**currency** | **str** | Currency of the repayment. | 
**fraction** | **float** | Fraction of the accrued on the holding to be repaid.  Must be between 0 and 1, inclusive.  Defaults to 1 if not set. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | Election for controlling whether the interest is paid automatically or not.  Exactly one election must be provided. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent | 
## Example

```python
from lusid.models.loan_interest_repayment_event import LoanInterestRepaymentEvent
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from datetime import datetime
payment_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
fraction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
lapse_elections: Optional[conlist(LapseElection)] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
loan_interest_repayment_event_instance = LoanInterestRepaymentEvent(payment_date=payment_date, ex_date=ex_date, currency=currency, fraction=fraction, lapse_elections=lapse_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

