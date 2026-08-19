# CoreRuleValues

A core matching rule and the values that pin a rec result to its reconciled position. These values  contribute to the result id.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_name** | **str** | The name of the rule. | 
**left_value** | **str** | The left-side value. | [optional] 
**right_value** | **str** | The right-side value. | [optional] 
**applied_tolerance** | [**ToleranceBase**](ToleranceBase.md) |  | [optional] 
## Example

```python
from lusid.models.core_rule_values import CoreRuleValues
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_name: StrictStr = "example_rule_name"
left_value: Optional[StrictStr] = "example_left_value"
right_value: Optional[StrictStr] = "example_right_value"
applied_tolerance: Optional[ToleranceBase] = # Replace with your value
core_rule_values_instance = CoreRuleValues(rule_name=rule_name, left_value=left_value, right_value=right_value, applied_tolerance=applied_tolerance)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

