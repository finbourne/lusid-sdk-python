# DeleteInstrumentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**as_at** | **datetime** | The as-at datetime at which the instrument was deleted. | 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.delete_instrument_response import DeleteInstrumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInstrumentResponse from a JSON string
delete_instrument_response_instance = DeleteInstrumentResponse.from_json(json)
# print the JSON string representation of the object
print DeleteInstrumentResponse.to_json()

# convert the object into a dict
delete_instrument_response_dict = delete_instrument_response_instance.to_dict()
# create an instance of DeleteInstrumentResponse from a dict
delete_instrument_response_form_dict = delete_instrument_response.from_dict(delete_instrument_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


