# Mapping

Defines the rule set to be used to determine if entries should be considered as a match.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope for this mapping. | 
**code** | **str** | The code for this mapping. | 
**name** | **str** | The mapping name | 
**reconciliation_type** | **str** | What type of reconciliation this mapping is for | 
**rules** | [**List[MappingRule]**](MappingRule.md) | The rules in this mapping, keyed by the left field/property name | [optional] 

## Example

```python
from lusid.models.mapping import Mapping

# TODO update the JSON string below
json = "{}"
# create an instance of Mapping from a JSON string
mapping_instance = Mapping.from_json(json)
# print the JSON string representation of the object
print Mapping.to_json()

# convert the object into a dict
mapping_dict = mapping_instance.to_dict()
# create an instance of Mapping from a dict
mapping_form_dict = mapping.from_dict(mapping_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


