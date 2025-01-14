# Alias


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The property key, identifier type, or field to be replaced by an alias. | 
**attribute_alias** | **str** | The alias to replace tPrecedencehe property key, identifier type, or field on the bound entity. | 

## Example

```python
from lusid.models.alias import Alias

# TODO update the JSON string below
json = "{}"
# create an instance of Alias from a JSON string
alias_instance = Alias.from_json(json)
# print the JSON string representation of the object
print Alias.to_json()

# convert the object into a dict
alias_dict = alias_instance.to_dict()
# create an instance of Alias from a dict
alias_form_dict = alias.from_dict(alias_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


