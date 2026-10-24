# MarginRun

A margin run: the valuation of the collateral agreements for a business date, planned as shards that report  their progress, and the margin calls and lines it has published so far.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URI of this margin run. | [optional] 
**id** | **str** | The identifier of the run: the effective date and the asAt it was valued at, with a suffix naming the scenario for a stress run. Filterable. | 
**effective_at** | **datetime** | The business date the run values collateral agreements for. Filterable. | 
**as_at** | **datetime** | The asAt datetime the run reads agreements, portfolios and market data at. Filterable. | 
**status** | **str** | The status of the run. One of Pending, Running, Completed or CompletedWithIssues. Filterable. | 
**agreements** | [**List[ResourceId]**](ResourceId.md) | The collateral agreements the run covers. | 
**call_count** | **int** | The number of margin calls the run has published so far. | 
**line_count** | **int** | The number of margin lines the run has published so far. | 
**shard_count** | **int** | The number of valuation shards the run was planned as. | 
**completed_shards** | **int** | The number of shards that have completed. | 
**failed_shards** | **int** | The number of shards that failed to value. | 
**issues** | [**List[MarginRunIssue]**](MarginRunIssue.md) | Agreements the run could not value or roll up into a call, or the caller may not calculate margin for, with the reason. | 
**shards** | [**List[MarginRunShard]**](MarginRunShard.md) | The valuation shards the run is planned as, with their progress. | 
**scenario** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.margin_run import MarginRun
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: StrictStr = "example_id"
effective_at: datetime = # Replace with your value
as_at: datetime = # Replace with your value
status: StrictStr = "example_status"
agreements: List[ResourceId] = # Replace with your value
call_count: StrictInt = # Replace with your value
call_count: StrictInt = 42
line_count: StrictInt = # Replace with your value
line_count: StrictInt = 42
shard_count: StrictInt = # Replace with your value
shard_count: StrictInt = 42
completed_shards: StrictInt = # Replace with your value
completed_shards: StrictInt = 42
failed_shards: StrictInt = # Replace with your value
failed_shards: StrictInt = 42
issues: List[MarginRunIssue] = # Replace with your value
shards: List[MarginRunShard] = # Replace with your value
scenario: Optional[ResourceId] = None
margin_run_instance = MarginRun(href=href, id=id, effective_at=effective_at, as_at=as_at, status=status, agreements=agreements, call_count=call_count, line_count=line_count, shard_count=shard_count, completed_shards=completed_shards, failed_shards=failed_shards, issues=issues, shards=shards, scenario=scenario)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

