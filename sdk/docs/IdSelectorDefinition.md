# IdSelectorDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **Dict[str, str]** |  | 
**actions** | [**List[ActionId]**](ActionId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from lusid.models.id_selector_definition import IdSelectorDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of IdSelectorDefinition from a JSON string
id_selector_definition_instance = IdSelectorDefinition.from_json(json)
# print the JSON string representation of the object
print IdSelectorDefinition.to_json()

# convert the object into a dict
id_selector_definition_dict = id_selector_definition_instance.to_dict()
# create an instance of IdSelectorDefinition from a dict
id_selector_definition_form_dict = id_selector_definition.from_dict(id_selector_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


