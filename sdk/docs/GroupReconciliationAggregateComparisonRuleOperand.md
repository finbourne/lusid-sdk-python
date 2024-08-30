# GroupReconciliationAggregateComparisonRuleOperand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the value to compare | 
**operation** | **str** | What to do with the value pointed to by the key, e.g. Sum. Only \&quot;Value is allowed for core rules\&quot; | 

## Example

```python
from lusid.models.group_reconciliation_aggregate_comparison_rule_operand import GroupReconciliationAggregateComparisonRuleOperand

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationAggregateComparisonRuleOperand from a JSON string
group_reconciliation_aggregate_comparison_rule_operand_instance = GroupReconciliationAggregateComparisonRuleOperand.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationAggregateComparisonRuleOperand.to_json()

# convert the object into a dict
group_reconciliation_aggregate_comparison_rule_operand_dict = group_reconciliation_aggregate_comparison_rule_operand_instance.to_dict()
# create an instance of GroupReconciliationAggregateComparisonRuleOperand from a dict
group_reconciliation_aggregate_comparison_rule_operand_form_dict = group_reconciliation_aggregate_comparison_rule_operand.from_dict(group_reconciliation_aggregate_comparison_rule_operand_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


