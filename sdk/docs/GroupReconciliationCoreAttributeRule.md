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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: GroupReconciliationCoreComparisonRuleOperand
right: GroupReconciliationCoreComparisonRuleOperand
allowable_string_mappings: Optional[List[GroupReconciliationComparisonRuleStringValueMap]] = # Replace with your value
is_comparison_case_sensitive: StrictBool = # Replace with your value
is_comparison_case_sensitive:StrictBool = True
group_reconciliation_core_attribute_rule_instance = GroupReconciliationCoreAttributeRule(left=left, right=right, allowable_string_mappings=allowable_string_mappings, is_comparison_case_sensitive=is_comparison_case_sensitive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

