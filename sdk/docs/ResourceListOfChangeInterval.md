# ResourceListOfChangeInterval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ChangeInterval]**](ChangeInterval.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_change_interval import ResourceListOfChangeInterval

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfChangeInterval from a JSON string
resource_list_of_change_interval_instance = ResourceListOfChangeInterval.from_json(json)
# print the JSON string representation of the object
print ResourceListOfChangeInterval.to_json()

# convert the object into a dict
resource_list_of_change_interval_dict = resource_list_of_change_interval_instance.to_dict()
# create an instance of ResourceListOfChangeInterval from a dict
resource_list_of_change_interval_form_dict = resource_list_of_change_interval.from_dict(resource_list_of_change_interval_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


