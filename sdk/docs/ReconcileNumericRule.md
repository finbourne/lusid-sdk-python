# ReconcileNumericRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_type** | **str** | The available values are: Exact, AbsoluteDifference, RelativeDifference | 
**tolerance** | **float** | For a numeric type only (i.e. decimal, integer, date or datetime offset possibly controversially), this is the quantity used in the comparison.  The units of the tolerance must be set appropriately for the item being compared.  For a number such as a currency or amount that will be a simple quantity, for a DateTime or DateTimeOffset it should be days. If fewer than a single day then this should be  passed as a fraction. | [optional] 
**applies_to** | [**AggregateSpec**](AggregateSpec.md) |  | 
**rule_type** | **str** | The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact | 
## Example

```python
from lusid.models.reconcile_numeric_rule import ReconcileNumericRule
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator

comparison_type: StrictStr = "example_comparison_type"
tolerance: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
applies_to: AggregateSpec = # Replace with your value
rule_type: StrictStr = "example_rule_type"
reconcile_numeric_rule_instance = ReconcileNumericRule(comparison_type=comparison_type, tolerance=tolerance, applies_to=applies_to, rule_type=rule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

