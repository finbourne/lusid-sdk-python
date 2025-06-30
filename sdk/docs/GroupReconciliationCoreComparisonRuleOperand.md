# GroupReconciliationCoreComparisonRuleOperand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the value to compare | 
**operation** | **str** | What to do with the value pointed to by the key, e.g. Sum. Only \&quot;Value is allowed for core rules\&quot; | 
## Example

```python
from lusid.models.group_reconciliation_core_comparison_rule_operand import GroupReconciliationCoreComparisonRuleOperand
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

key: StrictStr = "example_key"
operation: StrictStr = "example_operation"
group_reconciliation_core_comparison_rule_operand_instance = GroupReconciliationCoreComparisonRuleOperand(key=key, operation=operation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

