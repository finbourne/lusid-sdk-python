# MarginRunShard

One valuation shard of a margin run: the agreements it values with one recipe, and how far it has got.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the shard within the run. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**agreements** | [**List[ResourceId]**](ResourceId.md) | The collateral agreements the shard values. | 
**status** | **str** | The status of the shard. One of Pending, Running, Completed or Failed. | 
**call_count** | **int** | The number of margin calls the shard published. | 
**line_count** | **int** | The number of margin lines the shard published. | 
**detail** | **str** | Why the shard failed, or which of its netting sets it completed without figures and why. | [optional] 
**as_at** | **datetime** | When the shard was valued: the run&#39;s as-at, or the time of the retry that valued it. Null until the shard has finished. | [optional] 
## Example

```python
from lusid.models.margin_run_shard import MarginRunShard
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
recipe_id: Optional[ResourceId] = # Replace with your value
agreements: List[ResourceId] = # Replace with your value
status: StrictStr = "example_status"
call_count: StrictInt = # Replace with your value
call_count: StrictInt = 42
line_count: StrictInt = # Replace with your value
line_count: StrictInt = 42
detail: Optional[StrictStr] = "example_detail"
as_at: Optional[datetime] = # Replace with your value
margin_run_shard_instance = MarginRunShard(id=id, recipe_id=recipe_id, agreements=agreements, status=status, call_count=call_count, line_count=line_count, detail=detail, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

