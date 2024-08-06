# MappingRule

An individual mapping rule, for mapping between a left and right field/property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | The name of the field/property in the left resource (e.g. a transaction) | [optional] 
**right** | **str** | The name of the field/property in the right resource (e.g. a transaction) | [optional] 
**comparison_type** | **str** | The type of comparison to be performed | [optional] 
**comparison_value** | **float** | The (optional) value used with Finbourne.WebApi.Interface.Dto.Mappings.MappingRule.ComparisonType | [optional] 
**weight** | **float** | A factor used to influence the importance of this item. | [optional] 
**mapped_strings** | [**List[MappedString]**](MappedString.md) | The (optional) value used to map string values. | [optional] 
**is_case_sensitive** | **bool** | Should string comparisons take case into account, defaults to &#x60;false&#x60;. | [optional] 

## Example

```python
from lusid.models.mapping_rule import MappingRule

# TODO update the JSON string below
json = "{}"
# create an instance of MappingRule from a JSON string
mapping_rule_instance = MappingRule.from_json(json)
# print the JSON string representation of the object
print MappingRule.to_json()

# convert the object into a dict
mapping_rule_dict = mapping_rule_instance.to_dict()
# create an instance of MappingRule from a dict
mapping_rule_form_dict = mapping_rule.from_dict(mapping_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


