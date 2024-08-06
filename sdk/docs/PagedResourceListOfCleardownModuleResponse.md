# PagedResourceListOfCleardownModuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[CleardownModuleResponse]**](CleardownModuleResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_cleardown_module_response import PagedResourceListOfCleardownModuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfCleardownModuleResponse from a JSON string
paged_resource_list_of_cleardown_module_response_instance = PagedResourceListOfCleardownModuleResponse.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfCleardownModuleResponse.to_json()

# convert the object into a dict
paged_resource_list_of_cleardown_module_response_dict = paged_resource_list_of_cleardown_module_response_instance.to_dict()
# create an instance of PagedResourceListOfCleardownModuleResponse from a dict
paged_resource_list_of_cleardown_module_response_form_dict = paged_resource_list_of_cleardown_module_response.from_dict(paged_resource_list_of_cleardown_module_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


