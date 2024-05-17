# ResourceListOfApplicableInstrumentEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ApplicableInstrumentEvent]**](ApplicableInstrumentEvent.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_applicable_instrument_event import ResourceListOfApplicableInstrumentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfApplicableInstrumentEvent from a JSON string
resource_list_of_applicable_instrument_event_instance = ResourceListOfApplicableInstrumentEvent.from_json(json)
# print the JSON string representation of the object
print ResourceListOfApplicableInstrumentEvent.to_json()

# convert the object into a dict
resource_list_of_applicable_instrument_event_dict = resource_list_of_applicable_instrument_event_instance.to_dict()
# create an instance of ResourceListOfApplicableInstrumentEvent from a dict
resource_list_of_applicable_instrument_event_form_dict = resource_list_of_applicable_instrument_event.from_dict(resource_list_of_applicable_instrument_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


