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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, conlist

left: GroupReconciliationCoreComparisonRuleOperand = # Replace with your value
right: GroupReconciliationCoreComparisonRuleOperand = # Replace with your value
allowable_string_mappings: Optional[conlist(GroupReconciliationComparisonRuleStringValueMap)] = # Replace with your value
is_comparison_case_sensitive: StrictBool = # Replace with your value
is_comparison_case_sensitive:StrictBool = True
group_reconciliation_core_attribute_rule_instance = GroupReconciliationCoreAttributeRule(left=left, right=right, allowable_string_mappings=allowable_string_mappings, is_comparison_case_sensitive=is_comparison_case_sensitive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

