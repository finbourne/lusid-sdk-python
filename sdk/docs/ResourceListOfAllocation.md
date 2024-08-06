# ResourceListOfAllocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Allocation]**](Allocation.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_allocation import ResourceListOfAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfAllocation from a JSON string
resource_list_of_allocation_instance = ResourceListOfAllocation.from_json(json)
# print the JSON string representation of the object
print ResourceListOfAllocation.to_json()

# convert the object into a dict
resource_list_of_allocation_dict = resource_list_of_allocation_instance.to_dict()
# create an instance of ResourceListOfAllocation from a dict
resource_list_of_allocation_form_dict = resource_list_of_allocation.from_dict(resource_list_of_allocation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


