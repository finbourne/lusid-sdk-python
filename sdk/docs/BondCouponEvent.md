# BondCouponEvent

Definition of a Bond Coupon Event  This is an event that describes the occurence of a cashflow due to a fixed rate bond coupon payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | Ex-Dividend date of the coupon payment | 
**payment_date** | **datetime** | Payment date of the coupon payment | 
**currency** | **str** | Currency of the coupon payment | 
**coupon_per_unit** | **float** | CouponRate*Principal | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent | 

## Example

```python
from lusid.models.bond_coupon_event import BondCouponEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BondCouponEvent from a JSON string
bond_coupon_event_instance = BondCouponEvent.from_json(json)
# print the JSON string representation of the object
print BondCouponEvent.to_json()

# convert the object into a dict
bond_coupon_event_dict = bond_coupon_event_instance.to_dict()
# create an instance of BondCouponEvent from a dict
bond_coupon_event_form_dict = bond_coupon_event.from_dict(bond_coupon_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


