# ResourceListOfCorporateAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[CorporateAction]**](CorporateAction.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_corporate_action import ResourceListOfCorporateAction

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfCorporateAction from a JSON string
resource_list_of_corporate_action_instance = ResourceListOfCorporateAction.from_json(json)
# print the JSON string representation of the object
print ResourceListOfCorporateAction.to_json()

# convert the object into a dict
resource_list_of_corporate_action_dict = resource_list_of_corporate_action_instance.to_dict()
# create an instance of ResourceListOfCorporateAction from a dict
resource_list_of_corporate_action_form_dict = resource_list_of_corporate_action.from_dict(resource_list_of_corporate_action_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


