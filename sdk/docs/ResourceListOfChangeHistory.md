# ResourceListOfChangeHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ChangeHistory]**](ChangeHistory.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_change_history import ResourceListOfChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfChangeHistory from a JSON string
resource_list_of_change_history_instance = ResourceListOfChangeHistory.from_json(json)
# print the JSON string representation of the object
print ResourceListOfChangeHistory.to_json()

# convert the object into a dict
resource_list_of_change_history_dict = resource_list_of_change_history_instance.to_dict()
# create an instance of ResourceListOfChangeHistory from a dict
resource_list_of_change_history_form_dict = resource_list_of_change_history.from_dict(resource_list_of_change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


