# GroupReconciliationAggregateAttributeRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**GroupReconciliationAggregateComparisonRuleOperand**](GroupReconciliationAggregateComparisonRuleOperand.md) |  | 
**right** | [**GroupReconciliationAggregateComparisonRuleOperand**](GroupReconciliationAggregateComparisonRuleOperand.md) |  | 
**tolerance** | [**GroupReconciliationComparisonRuleTolerance**](GroupReconciliationComparisonRuleTolerance.md) |  | 

## Example

```python
from lusid.models.group_reconciliation_aggregate_attribute_rule import GroupReconciliationAggregateAttributeRule

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationAggregateAttributeRule from a JSON string
group_reconciliation_aggregate_attribute_rule_instance = GroupReconciliationAggregateAttributeRule.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationAggregateAttributeRule.to_json()

# convert the object into a dict
group_reconciliation_aggregate_attribute_rule_dict = group_reconciliation_aggregate_attribute_rule_instance.to_dict()
# create an instance of GroupReconciliationAggregateAttributeRule from a dict
group_reconciliation_aggregate_attribute_rule_form_dict = group_reconciliation_aggregate_attribute_rule.from_dict(group_reconciliation_aggregate_attribute_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


