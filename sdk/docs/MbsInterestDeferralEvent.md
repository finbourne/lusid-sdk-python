# MbsInterestDeferralEvent

Definition of an MBS Interest Deferral Event This is an event that describes the occurence of a cashflow due to unpaid interest that was deferred and capitalised into the outstanding principal balance of a mortgage-backed security.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex date (entitlement date) of the interest payment, usually several weeks prior to the payment date | [optional] 
**payment_date** | **datetime** | The payment date of the interest that is deferred and capitalised | [optional] 
**currency** | **str** | The currency in which the interest amount is notated | 
**interest_per_unit** | **float** | The interest amount to be deferred and capitalised for each unit of the instrument held on the ex date | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent | 
## Example

```python
from lusid.models.mbs_interest_deferral_event import MbsInterestDeferralEvent
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from datetime import datetime
ex_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
interest_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
mbs_interest_deferral_event_instance = MbsInterestDeferralEvent(ex_date=ex_date, payment_date=payment_date, currency=currency, interest_per_unit=interest_per_unit, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

