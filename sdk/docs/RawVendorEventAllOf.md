# RawVendorEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective date of the event | 
**event_value** | [**LifeCycleEventValue**](LifeCycleEventValue.md) |  | 
**event_type** | **str** | What type of internal event does this represent; reset, exercise, amortisation etc. | 
**event_status** | **str** | What is the event status, is it a known (ie historic) or unknown (ie projected) event? | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.raw_vendor_event_all_of import RawVendorEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of RawVendorEventAllOf from a JSON string
raw_vendor_event_all_of_instance = RawVendorEventAllOf.from_json(json)
# print the JSON string representation of the object
print RawVendorEventAllOf.to_json()

# convert the object into a dict
raw_vendor_event_all_of_dict = raw_vendor_event_all_of_instance.to_dict()
# create an instance of RawVendorEventAllOf from a dict
raw_vendor_event_all_of_form_dict = raw_vendor_event_all_of.from_dict(raw_vendor_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


