# MarginRunAllocation

How far the allocation pass over a run's base calls got: whether it ran, how many calls it proposed collateral  for, and what it left out.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | How far the allocation pass got. One of Pending, Completed, Skipped or Failed. | 
**allocated_call_count** | **int** | How many calls the pass proposed collateral for. | 
**detail** | **str** | Which calls the pass could not allocate and why, or why it failed. Null when every call that moves our collateral was allocated. | [optional] 
## Example

```python
from lusid.models.margin_run_allocation import MarginRunAllocation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: StrictStr = "example_status"
allocated_call_count: StrictInt = # Replace with your value
allocated_call_count: StrictInt = 42
detail: Optional[StrictStr] = "example_detail"
margin_run_allocation_instance = MarginRunAllocation(status=status, allocated_call_count=allocated_call_count, detail=detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

