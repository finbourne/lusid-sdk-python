# RawVendorEvent

A generic event derived from the economic definition of an instrument. This should be considered purely  informational; any data provided by this event is not guaranteed to be processable by LUSID.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective date of the event | 
**event_value** | [**LifeCycleEventValue**](LifeCycleEventValue.md) |  | 
**event_type** | **str** | What type of internal event does this represent; reset, exercise, amortisation etc. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent | 

## Example

```python
from lusid.models.raw_vendor_event import RawVendorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RawVendorEvent from a JSON string
raw_vendor_event_instance = RawVendorEvent.from_json(json)
# print the JSON string representation of the object
print RawVendorEvent.to_json()

# convert the object into a dict
raw_vendor_event_dict = raw_vendor_event_instance.to_dict()
# create an instance of RawVendorEvent from a dict
raw_vendor_event_form_dict = raw_vendor_event.from_dict(raw_vendor_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


