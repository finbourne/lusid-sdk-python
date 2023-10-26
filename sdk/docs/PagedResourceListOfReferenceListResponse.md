# PagedResourceListOfReferenceListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[ReferenceListResponse]**](ReferenceListResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_reference_list_response import PagedResourceListOfReferenceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfReferenceListResponse from a JSON string
paged_resource_list_of_reference_list_response_instance = PagedResourceListOfReferenceListResponse.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfReferenceListResponse.to_json()

# convert the object into a dict
paged_resource_list_of_reference_list_response_dict = paged_resource_list_of_reference_list_response_instance.to_dict()
# create an instance of PagedResourceListOfReferenceListResponse from a dict
paged_resource_list_of_reference_list_response_form_dict = paged_resource_list_of_reference_list_response.from_dict(paged_resource_list_of_reference_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


