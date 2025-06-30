# GroupReconciliationAggregateAttributeRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**GroupReconciliationAggregateComparisonRuleOperand**](GroupReconciliationAggregateComparisonRuleOperand.md) |  | 
**right** | [**GroupReconciliationAggregateComparisonRuleOperand**](GroupReconciliationAggregateComparisonRuleOperand.md) |  | 
**tolerance** | [**GroupReconciliationComparisonRuleTolerance**](GroupReconciliationComparisonRuleTolerance.md) |  | [optional] 
## Example

```python
from lusid.models.group_reconciliation_aggregate_attribute_rule import GroupReconciliationAggregateAttributeRule
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

left: GroupReconciliationAggregateComparisonRuleOperand = # Replace with your value
right: GroupReconciliationAggregateComparisonRuleOperand = # Replace with your value
tolerance: Optional[GroupReconciliationComparisonRuleTolerance] = None
group_reconciliation_aggregate_attribute_rule_instance = GroupReconciliationAggregateAttributeRule(left=left, right=right, tolerance=tolerance)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

