# CloseEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The first date on which the instrument could close | [optional] 
**end_date** | **datetime** | The last date on which the instrument could close | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.close_event_all_of import CloseEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CloseEventAllOf from a JSON string
close_event_all_of_instance = CloseEventAllOf.from_json(json)
# print the JSON string representation of the object
print CloseEventAllOf.to_json()

# convert the object into a dict
close_event_all_of_dict = close_event_all_of_instance.to_dict()
# create an instance of CloseEventAllOf from a dict
close_event_all_of_form_dict = close_event_all_of.from_dict(close_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


