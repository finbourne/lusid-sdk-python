# ReferenceListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The name of the reference list. | 
**description** | **str** | The description of the reference list. | [optional] 
**tags** | **List[str]** | The tags associated with the reference list. | [optional] 
**reference_list** | [**ReferenceList**](ReferenceList.md) |  | 
**version** | [**Version**](Version.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.reference_list_response import ReferenceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceListResponse from a JSON string
reference_list_response_instance = ReferenceListResponse.from_json(json)
# print the JSON string representation of the object
print ReferenceListResponse.to_json()

# convert the object into a dict
reference_list_response_dict = reference_list_response_instance.to_dict()
# create an instance of ReferenceListResponse from a dict
reference_list_response_form_dict = reference_list_response.from_dict(reference_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


