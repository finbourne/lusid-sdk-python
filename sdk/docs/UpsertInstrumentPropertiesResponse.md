# UpsertInstrumentPropertiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_date** | **datetime** | The as-at datetime at which properties were created or updated. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_instrument_properties_response import UpsertInstrumentPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertInstrumentPropertiesResponse from a JSON string
upsert_instrument_properties_response_instance = UpsertInstrumentPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print UpsertInstrumentPropertiesResponse.to_json()

# convert the object into a dict
upsert_instrument_properties_response_dict = upsert_instrument_properties_response_instance.to_dict()
# create an instance of UpsertInstrumentPropertiesResponse from a dict
upsert_instrument_properties_response_form_dict = upsert_instrument_properties_response.from_dict(upsert_instrument_properties_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


