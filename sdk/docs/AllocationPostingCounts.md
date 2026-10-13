# AllocationPostingCounts

How many postings a plan writes on each side.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lp_side** | **int** | The number of instrument events on investors&#39; lines. | [optional] 
**roll_ups** | **int** | The number of roll-ups. | [optional] 
**fund_side** | **int** | The number of fund-side transactions. | [optional] 
## Example

```python
from lusid.models.allocation_posting_counts import AllocationPostingCounts
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lp_side: Optional[StrictInt] = # Replace with your value
lp_side: Optional[StrictInt] = None
roll_ups: Optional[StrictInt] = # Replace with your value
roll_ups: Optional[StrictInt] = None
fund_side: Optional[StrictInt] = # Replace with your value
fund_side: Optional[StrictInt] = None
allocation_posting_counts_instance = AllocationPostingCounts(lp_side=lp_side, roll_ups=roll_ups, fund_side=fund_side)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

