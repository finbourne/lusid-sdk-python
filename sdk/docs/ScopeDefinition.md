# ScopeDefinition

A list of scopes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The unique identifier for the scope. | 

## Example

```python
from lusid.models.scope_definition import ScopeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeDefinition from a JSON string
scope_definition_instance = ScopeDefinition.from_json(json)
# print the JSON string representation of the object
print ScopeDefinition.to_json()

# convert the object into a dict
scope_definition_dict = scope_definition_instance.to_dict()
# create an instance of ScopeDefinition from a dict
scope_definition_form_dict = scope_definition.from_dict(scope_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


