# DeleteInstrumentsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**as_at** | **datetime** | The as-at datetime at which the instrument was deleted. | 
**staged** | [**Dict[str, StagedModificationsInfo]**](StagedModificationsInfo.md) | Information about the pending staged modifications for the current entity. | [optional] [readonly] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.delete_instruments_response import DeleteInstrumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInstrumentsResponse from a JSON string
delete_instruments_response_instance = DeleteInstrumentsResponse.from_json(json)
# print the JSON string representation of the object
print DeleteInstrumentsResponse.to_json()

# convert the object into a dict
delete_instruments_response_dict = delete_instruments_response_instance.to_dict()
# create an instance of DeleteInstrumentsResponse from a dict
delete_instruments_response_form_dict = delete_instruments_response.from_dict(delete_instruments_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


