# TaxRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A user-friendly name | 
**description** | **str** | A description for this rule | 
**rate** | **float** | The rate to be applied if all criteria are met | 
**match_criteria** | [**List[MatchCriterion]**](MatchCriterion.md) | A set of criteria to be met for this rule to be applied | 

## Example

```python
from lusid.models.tax_rule import TaxRule

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRule from a JSON string
tax_rule_instance = TaxRule.from_json(json)
# print the JSON string representation of the object
print TaxRule.to_json()

# convert the object into a dict
tax_rule_dict = tax_rule_instance.to_dict()
# create an instance of TaxRule from a dict
tax_rule_form_dict = tax_rule.from_dict(tax_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


