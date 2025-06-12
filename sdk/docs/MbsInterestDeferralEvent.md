# MbsInterestDeferralEvent

Definition of an MBS Interest Deferral Event  This is an event that describes the occurence of a cashflow due to unpaid interest that was deferred and  capitalised into the outstanding principal balance of a mortgage-backed security.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex date (entitlement date) of the interest payment, usually several weeks prior to the payment date | [optional] 
**payment_date** | **datetime** | The payment date of the interest that is deferred and capitalised | [optional] 
**currency** | **str** | The currency in which the interest amount is notated | 
**interest_per_unit** | **float** | The interest amount to be deferred and capitalised for each unit of the instrument held on the ex date | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent | 

## Example

```python
from lusid.models.mbs_interest_deferral_event import MbsInterestDeferralEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MbsInterestDeferralEvent from a JSON string
mbs_interest_deferral_event_instance = MbsInterestDeferralEvent.from_json(json)
# print the JSON string representation of the object
print MbsInterestDeferralEvent.to_json()

# convert the object into a dict
mbs_interest_deferral_event_dict = mbs_interest_deferral_event_instance.to_dict()
# create an instance of MbsInterestDeferralEvent from a dict
mbs_interest_deferral_event_form_dict = mbs_interest_deferral_event.from_dict(mbs_interest_deferral_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


