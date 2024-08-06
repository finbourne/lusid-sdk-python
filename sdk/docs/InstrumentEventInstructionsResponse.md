# InstrumentEventInstructionsResponse

The collection of successfully upserted instructions, and the collection of failures for those instructions that could not be upserted

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, InstrumentEventInstruction]**](InstrumentEventInstruction.md) | The collection of successfully upserted instructions | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The collection of error information for instructions that could not be upserted | [optional] 

## Example

```python
from lusid.models.instrument_event_instructions_response import InstrumentEventInstructionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentEventInstructionsResponse from a JSON string
instrument_event_instructions_response_instance = InstrumentEventInstructionsResponse.from_json(json)
# print the JSON string representation of the object
print InstrumentEventInstructionsResponse.to_json()

# convert the object into a dict
instrument_event_instructions_response_dict = instrument_event_instructions_response_instance.to_dict()
# create an instance of InstrumentEventInstructionsResponse from a dict
instrument_event_instructions_response_form_dict = instrument_event_instructions_response.from_dict(instrument_event_instructions_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


