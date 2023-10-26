# TaxRuleSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | A user-friendly name | 
**description** | **str** | A description of what this rule set is for | 
**output_property_key** | **str** | The property key that this rule set will write to | 
**rules** | [**List[TaxRule]**](TaxRule.md) | The rules of this rule set, which stipulate what rate to apply (i.e. write to the OutputPropertyKey) under certain conditions | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.tax_rule_set import TaxRuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRuleSet from a JSON string
tax_rule_set_instance = TaxRuleSet.from_json(json)
# print the JSON string representation of the object
print TaxRuleSet.to_json()

# convert the object into a dict
tax_rule_set_dict = tax_rule_set_instance.to_dict()
# create an instance of TaxRuleSet from a dict
tax_rule_set_form_dict = tax_rule_set.from_dict(tax_rule_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


