# TransitionEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The announcement date of the corporate action | [optional] 
**ex_date** | **datetime** | The ex date of the corporate action | [optional] 
**record_date** | **datetime** | The record date of the corporate action | [optional] 
**payment_date** | **datetime** | The payment date of the corporate action | [optional] 
**input_transition** | [**InputTransition**](InputTransition.md) |  | [optional] 
**output_transitions** | [**List[OutputTransition]**](OutputTransition.md) | The resulting transitions from this event | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.transition_event_all_of import TransitionEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of TransitionEventAllOf from a JSON string
transition_event_all_of_instance = TransitionEventAllOf.from_json(json)
# print the JSON string representation of the object
print TransitionEventAllOf.to_json()

# convert the object into a dict
transition_event_all_of_dict = transition_event_all_of_instance.to_dict()
# create an instance of TransitionEventAllOf from a dict
transition_event_all_of_form_dict = transition_event_all_of.from_dict(transition_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


