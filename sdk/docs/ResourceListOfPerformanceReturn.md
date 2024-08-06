# ResourceListOfPerformanceReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[PerformanceReturn]**](PerformanceReturn.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_performance_return import ResourceListOfPerformanceReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfPerformanceReturn from a JSON string
resource_list_of_performance_return_instance = ResourceListOfPerformanceReturn.from_json(json)
# print the JSON string representation of the object
print ResourceListOfPerformanceReturn.to_json()

# convert the object into a dict
resource_list_of_performance_return_dict = resource_list_of_performance_return_instance.to_dict()
# create an instance of ResourceListOfPerformanceReturn from a dict
resource_list_of_performance_return_form_dict = resource_list_of_performance_return.from_dict(resource_list_of_performance_return_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


