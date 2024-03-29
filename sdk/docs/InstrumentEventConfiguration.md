# InstrumentEventConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_template_scopes** | **List[str]** |  | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.instrument_event_configuration import InstrumentEventConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentEventConfiguration from a JSON string
instrument_event_configuration_instance = InstrumentEventConfiguration.from_json(json)
# print the JSON string representation of the object
print InstrumentEventConfiguration.to_json()

# convert the object into a dict
instrument_event_configuration_dict = instrument_event_configuration_instance.to_dict()
# create an instance of InstrumentEventConfiguration from a dict
instrument_event_configuration_form_dict = instrument_event_configuration.from_dict(instrument_event_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


