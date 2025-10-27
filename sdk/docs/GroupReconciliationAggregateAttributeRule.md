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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: GroupReconciliationAggregateComparisonRuleOperand
right: GroupReconciliationAggregateComparisonRuleOperand
tolerance: Optional[GroupReconciliationComparisonRuleTolerance] = None
group_reconciliation_aggregate_attribute_rule_instance = GroupReconciliationAggregateAttributeRule(left=left, right=right, tolerance=tolerance)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

