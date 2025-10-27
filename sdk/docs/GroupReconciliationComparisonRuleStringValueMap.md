# GroupReconciliationComparisonRuleStringValueMap

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_value** | **str** | The left string to map | 
**right_value** | **str** | The right string to map | 
**direction** | **str** | The direction to map. \&quot;UniDirectional\&quot; | \&quot;BiDirectional\&quot; | 
## Example

```python
from lusid.models.group_reconciliation_comparison_rule_string_value_map import GroupReconciliationComparisonRuleStringValueMap
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left_value: StrictStr = "example_left_value"
right_value: StrictStr = "example_right_value"
direction: StrictStr = "example_direction"
group_reconciliation_comparison_rule_string_value_map_instance = GroupReconciliationComparisonRuleStringValueMap(left_value=left_value, right_value=right_value, direction=direction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

