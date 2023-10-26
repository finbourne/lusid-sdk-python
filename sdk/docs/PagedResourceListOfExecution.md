# PagedResourceListOfExecution


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Execution]**](Execution.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_execution import PagedResourceListOfExecution

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfExecution from a JSON string
paged_resource_list_of_execution_instance = PagedResourceListOfExecution.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfExecution.to_json()

# convert the object into a dict
paged_resource_list_of_execution_dict = paged_resource_list_of_execution_instance.to_dict()
# create an instance of PagedResourceListOfExecution from a dict
paged_resource_list_of_execution_form_dict = paged_resource_list_of_execution.from_dict(paged_resource_list_of_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


