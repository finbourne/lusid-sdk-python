# MbsInterestShortfallEvent

Definition of an MBS Interest Shortfall Event  This is an event that describes the occurence of a cashflow due to unpaid interest that was deferred and  not capitalised into the outstanding principal balance of a mortgage-backed security.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex date (entitlement date) of the interest payment, usually several weeks prior to the payment date | 
**payment_date** | **datetime** | The payment date of the interest | 
**currency** | **str** | The currency in which the interest amount is notated | 
**interest_per_unit** | **float** | The amount by which the coupon amount will fall short for each unit of the instrument held on the ex date | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent | 

## Example

```python
from lusid.models.mbs_interest_shortfall_event import MbsInterestShortfallEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MbsInterestShortfallEvent from a JSON string
mbs_interest_shortfall_event_instance = MbsInterestShortfallEvent.from_json(json)
# print the JSON string representation of the object
print MbsInterestShortfallEvent.to_json()

# convert the object into a dict
mbs_interest_shortfall_event_dict = mbs_interest_shortfall_event_instance.to_dict()
# create an instance of MbsInterestShortfallEvent from a dict
mbs_interest_shortfall_event_form_dict = mbs_interest_shortfall_event.from_dict(mbs_interest_shortfall_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


