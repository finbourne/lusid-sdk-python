# AggregateRuleValues

An aggregate matching rule and its values. The difference is the measured magnitude compared against  any applied tolerance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_name** | **str** | The name of the rule. | 
**left_value** | **str** | The left-side value. | [optional] 
**right_value** | **str** | The right-side value. | [optional] 
**difference** | **str** | The measured magnitude of the difference, ToString(ABS(leftValue - rightValue)). | 
**applied_tolerance** | [**ToleranceBase**](ToleranceBase.md) |  | [optional] 
## Example

```python
from lusid.models.aggregate_rule_values import AggregateRuleValues
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_name: StrictStr = "example_rule_name"
left_value: Optional[StrictStr] = "example_left_value"
right_value: Optional[StrictStr] = "example_right_value"
difference: StrictStr = "example_difference"
applied_tolerance: Optional[ToleranceBase] = # Replace with your value
aggregate_rule_values_instance = AggregateRuleValues(rule_name=rule_name, left_value=left_value, right_value=right_value, difference=difference, applied_tolerance=applied_tolerance)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

