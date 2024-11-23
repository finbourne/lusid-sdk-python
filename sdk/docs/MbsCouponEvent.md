# MbsCouponEvent

Definition of an MBS Coupon Event  This is an event that describes the occurence of a cashflow due to a mortgage-backed security coupon payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex date (entitlement date) of the coupon | 
**payment_date** | **datetime** | The payment date of the coupon | 
**currency** | **str** | The currency in which the coupon is paid | 
**coupon_per_unit** | **float** | The coupon amount received for each unit of the instrument held on the ex date | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent | 

## Example

```python
from lusid.models.mbs_coupon_event import MbsCouponEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MbsCouponEvent from a JSON string
mbs_coupon_event_instance = MbsCouponEvent.from_json(json)
# print the JSON string representation of the object
print MbsCouponEvent.to_json()

# convert the object into a dict
mbs_coupon_event_dict = mbs_coupon_event_instance.to_dict()
# create an instance of MbsCouponEvent from a dict
mbs_coupon_event_form_dict = mbs_coupon_event.from_dict(mbs_coupon_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


