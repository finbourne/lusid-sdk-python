# OrderRuleBreach

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach_task_id** | **str** | Uniquely identifies this historical order breach workflow task. | 
**compliance_state** | **str** | The compliance state of this order breach. Possible values are &#39;Pending&#39;, &#39;Failed&#39;, &#39;Manually approved&#39;, &#39;Passed&#39; and &#39;Warning&#39;. | 
## Example

```python
from lusid.models.order_rule_breach import OrderRuleBreach
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

breach_task_id: StrictStr = "example_breach_task_id"
compliance_state: StrictStr = "example_compliance_state"
order_rule_breach_instance = OrderRuleBreach(breach_task_id=breach_task_id, compliance_state=compliance_state)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

