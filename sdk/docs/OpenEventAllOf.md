# OpenEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor_date** | **datetime** | The date on the which the instrument was opened. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.open_event_all_of import OpenEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of OpenEventAllOf from a JSON string
open_event_all_of_instance = OpenEventAllOf.from_json(json)
# print the JSON string representation of the object
print OpenEventAllOf.to_json()

# convert the object into a dict
open_event_all_of_dict = open_event_all_of_instance.to_dict()
# create an instance of OpenEventAllOf from a dict
open_event_all_of_form_dict = open_event_all_of.from_dict(open_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


