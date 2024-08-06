# UpsertInstrumentEventsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, InstrumentEventHolder]**](InstrumentEventHolder.md) | The corporate actions which have been successfully updated or inserted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The corporate actions that could not be updated or inserted along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_instrument_events_response import UpsertInstrumentEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertInstrumentEventsResponse from a JSON string
upsert_instrument_events_response_instance = UpsertInstrumentEventsResponse.from_json(json)
# print the JSON string representation of the object
print UpsertInstrumentEventsResponse.to_json()

# convert the object into a dict
upsert_instrument_events_response_dict = upsert_instrument_events_response_instance.to_dict()
# create an instance of UpsertInstrumentEventsResponse from a dict
upsert_instrument_events_response_form_dict = upsert_instrument_events_response.from_dict(upsert_instrument_events_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


