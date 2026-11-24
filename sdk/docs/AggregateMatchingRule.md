# AggregateMatchingRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_name** | **str** | The reference name of the rule. | 
**left_formula** | **str** | Derivation formula evaluated against the left side of the reconciliation. | 
**left_operation** | **str** | Group-level operation applied to the left side&#39;s per-item values during reconciliation. Sum adds up decimal values. UniformValue requires all items on the side to carry the same value of any type, and compares it with the other side&#39;s value. UniformValue must be used on both sides or on neither. Available values: Sum, UniformValue. | 
**right_formula** | **str** | Derivation formula evaluated against the right side of the reconciliation. | 
**right_operation** | **str** | Group-level operation applied to the right side&#39;s per-item values during reconciliation. Sum adds up decimal values. UniformValue requires all items on the side to carry the same value of any type, and compares it with the other side&#39;s value. UniformValue must be used on both sides or on neither. Available values: Sum, UniformValue. | 
**is_case_sensitive** | **bool** | Whether the comparison of a string rule is case sensitive. Optional, defaults to false. Only a rule whose values are strings can declare it. | [optional] 
## Example

```python
from lusid.models.aggregate_matching_rule import AggregateMatchingRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_name: StrictStr = "example_rule_name"
left_formula: StrictStr = "example_left_formula"
left_operation: StrictStr = "example_left_operation"
right_formula: StrictStr = "example_right_formula"
right_operation: StrictStr = "example_right_operation"
is_case_sensitive: Optional[StrictBool] = # Replace with your value
is_case_sensitive:Optional[StrictBool] = None
aggregate_matching_rule_instance = AggregateMatchingRule(rule_name=rule_name, left_formula=left_formula, left_operation=left_operation, right_formula=right_formula, right_operation=right_operation, is_case_sensitive=is_case_sensitive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

