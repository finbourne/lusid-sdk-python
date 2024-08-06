# AccessControlledAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**action** | [**ActionId**](ActionId.md) |  | 
**limited_set** | [**List[IdSelectorDefinition]**](IdSelectorDefinition.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.access_controlled_action import AccessControlledAction

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlledAction from a JSON string
access_controlled_action_instance = AccessControlledAction.from_json(json)
# print the JSON string representation of the object
print AccessControlledAction.to_json()

# convert the object into a dict
access_controlled_action_dict = access_controlled_action_instance.to_dict()
# create an instance of AccessControlledAction from a dict
access_controlled_action_form_dict = access_controlled_action.from_dict(access_controlled_action_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


