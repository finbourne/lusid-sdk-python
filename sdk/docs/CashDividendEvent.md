# CashDividendEvent

A cash distribution paid out to shareholders.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The date the company begins distributing the dividend. | [optional] 
**ex_date** | **datetime** | The first business day on which the dividend is not owed to the buying party. | [optional] 
**cash_elections** | [**List[CashElection]**](CashElection.md) | Possible elections for this event, each keyed with a unique identifier. | 
**announcement_date** | **datetime** | Date on which the dividend is announced by the company. | [optional] 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent | 
## Example

```python
from lusid.models.cash_dividend_event import CashDividendEvent
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictStr, conlist, validator
from datetime import datetime
payment_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
cash_elections: conlist(CashElection) = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
cash_dividend_event_instance = CashDividendEvent(payment_date=payment_date, ex_date=ex_date, cash_elections=cash_elections, announcement_date=announcement_date, record_date=record_date, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

