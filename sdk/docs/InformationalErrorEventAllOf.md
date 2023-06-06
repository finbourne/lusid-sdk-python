# InformationalErrorEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_detail** | **str** | The details of the error | 
**error_reason** | **str** | The error reason | 
**effective_at** | **datetime** | The effective date of the evaulation | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.informational_error_event_all_of import InformationalErrorEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of InformationalErrorEventAllOf from a JSON string
informational_error_event_all_of_instance = InformationalErrorEventAllOf.from_json(json)
# print the JSON string representation of the object
print InformationalErrorEventAllOf.to_json()

# convert the object into a dict
informational_error_event_all_of_dict = informational_error_event_all_of_instance.to_dict()
# create an instance of InformationalErrorEventAllOf from a dict
informational_error_event_all_of_form_dict = informational_error_event_all_of.from_dict(informational_error_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


