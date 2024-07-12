# ComponentRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_criteria** | **str** |  | 
**components** | **Dict[str, str]** |  | [optional] 

## Example

```python
from lusid.models.component_rule import ComponentRule

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentRule from a JSON string
component_rule_instance = ComponentRule.from_json(json)
# print the JSON string representation of the object
print ComponentRule.to_json()

# convert the object into a dict
component_rule_dict = component_rule_instance.to_dict()
# create an instance of ComponentRule from a dict
component_rule_form_dict = component_rule.from_dict(component_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


