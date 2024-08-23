# GeneratedEventDiagnostics

Represents a set of diagnostics per generatedEvent, where applicable.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_id** | **str** |  | 
**type** | **str** |  | 
**detail** | **str** |  | 
**error_details** | **List[str]** |  | 

## Example

```python
from lusid.models.generated_event_diagnostics import GeneratedEventDiagnostics

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratedEventDiagnostics from a JSON string
generated_event_diagnostics_instance = GeneratedEventDiagnostics.from_json(json)
# print the JSON string representation of the object
print GeneratedEventDiagnostics.to_json()

# convert the object into a dict
generated_event_diagnostics_dict = generated_event_diagnostics_instance.to_dict()
# create an instance of GeneratedEventDiagnostics from a dict
generated_event_diagnostics_form_dict = generated_event_diagnostics.from_dict(generated_event_diagnostics_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


