# GroupReconciliationComparisonRuleTolerance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of tolerance to allow. \&quot;Relative\&quot; | \&quot;Absolute\&quot; | 
**value** | **float** | The decimal value of how much tolerance to allow when comparing in relative (i.e percentage) or absolute terms depending on the ToleranceType specified | 
## Example

```python
from lusid.models.group_reconciliation_comparison_rule_tolerance import GroupReconciliationComparisonRuleTolerance
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, constr

type: StrictStr = "example_type"
value: Union[StrictFloat, StrictInt] = # Replace with your value
group_reconciliation_comparison_rule_tolerance_instance = GroupReconciliationComparisonRuleTolerance(type=type, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

