# ExpiryEvent

Definition of an Expiry Event  This is an event that describes the expiry of the instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **datetime** | Expiry date of the instrument | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent | 

## Example

```python
from lusid.models.expiry_event import ExpiryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiryEvent from a JSON string
expiry_event_instance = ExpiryEvent.from_json(json)
# print the JSON string representation of the object
print ExpiryEvent.to_json()

# convert the object into a dict
expiry_event_dict = expiry_event_instance.to_dict()
# create an instance of ExpiryEvent from a dict
expiry_event_form_dict = expiry_event.from_dict(expiry_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


