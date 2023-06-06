# ResourceListOfExecution


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Execution]**](Execution.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_execution import ResourceListOfExecution

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfExecution from a JSON string
resource_list_of_execution_instance = ResourceListOfExecution.from_json(json)
# print the JSON string representation of the object
print ResourceListOfExecution.to_json()

# convert the object into a dict
resource_list_of_execution_dict = resource_list_of_execution_instance.to_dict()
# create an instance of ResourceListOfExecution from a dict
resource_list_of_execution_form_dict = resource_list_of_execution.from_dict(resource_list_of_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


