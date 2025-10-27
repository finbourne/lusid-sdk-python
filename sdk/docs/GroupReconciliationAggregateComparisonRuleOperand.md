# GroupReconciliationAggregateComparisonRuleOperand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the value to compare | 
**operation** | **str** | What to do with the value pointed to by the key, e.g. Sum. Only \&quot;Value is allowed for core rules\&quot; | 
## Example

```python
from lusid.models.group_reconciliation_aggregate_comparison_rule_operand import GroupReconciliationAggregateComparisonRuleOperand
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
operation: StrictStr = "example_operation"
group_reconciliation_aggregate_comparison_rule_operand_instance = GroupReconciliationAggregateComparisonRuleOperand(key=key, operation=operation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

