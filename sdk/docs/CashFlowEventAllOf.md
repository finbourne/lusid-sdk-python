# CashFlowEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_flow_value** | [**CashFlowValue**](CashFlowValue.md) |  | 
**event_type** | **str** | What type of internal event does this represent; coupon, principal, premium etc. | [readonly] 
**event_status** | **str** | What is the event status, is it a known (ie historic) or unknown (ie projected) event? | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.cash_flow_event_all_of import CashFlowEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowEventAllOf from a JSON string
cash_flow_event_all_of_instance = CashFlowEventAllOf.from_json(json)
# print the JSON string representation of the object
print CashFlowEventAllOf.to_json()

# convert the object into a dict
cash_flow_event_all_of_dict = cash_flow_event_all_of_instance.to_dict()
# create an instance of CashFlowEventAllOf from a dict
cash_flow_event_all_of_form_dict = cash_flow_event_all_of.from_dict(cash_flow_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


