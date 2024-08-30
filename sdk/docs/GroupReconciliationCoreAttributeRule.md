# GroupReconciliationCoreAttributeRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**GroupReconciliationCoreComparisonRuleOperand**](GroupReconciliationCoreComparisonRuleOperand.md) |  | 
**right** | [**GroupReconciliationCoreComparisonRuleOperand**](GroupReconciliationCoreComparisonRuleOperand.md) |  | 
**allowable_string_mappings** | [**List[GroupReconciliationComparisonRuleStringValueMap]**](GroupReconciliationComparisonRuleStringValueMap.md) | The string mappings to use when comparing | [optional] 
**is_comparison_case_sensitive** | **bool** | Whether the compare keys and strings mappings case sensitive or not | 

## Example

```python
from lusid.models.group_reconciliation_core_attribute_rule import GroupReconciliationCoreAttributeRule

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationCoreAttributeRule from a JSON string
group_reconciliation_core_attribute_rule_instance = GroupReconciliationCoreAttributeRule.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationCoreAttributeRule.to_json()

# convert the object into a dict
group_reconciliation_core_attribute_rule_dict = group_reconciliation_core_attribute_rule_instance.to_dict()
# create an instance of GroupReconciliationCoreAttributeRule from a dict
group_reconciliation_core_attribute_rule_form_dict = group_reconciliation_core_attribute_rule.from_dict(group_reconciliation_core_attribute_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


