# PartnerAllocationRunResult

The outcome of a partner allocation run: the pools the period's income was split into and what, if anything,  could not be attributed to a pool.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | 
**period_start** | **datetime** | The start of the period to allocate, exclusive. | 
**period_end** | **datetime** | The end of the period to allocate, inclusive. A valuation point must end on this date. | 
**nav_type_code** | **str** | The NAV type to allocate under. Defaults to the fund&#39;s primary NAV type. | 
**status** | **str** | The outcome of the run. Available values: Computed, Booked, DryRun. | 
**run_id** | **str** | The identifier of the run, which prefixes every transaction it books. | 
**pools** | [**List[PartnerAllocationPool]**](PartnerAllocationPool.md) | The pools of fund-level amount that were allocated. | 
**unattributed** | [**List[UnattributedAmount]**](UnattributedAmount.md) | Fund-level amounts that no pool claimed. | 
**booked_transaction_ids** | **List[str]** | The identifiers of the transactions the run booked, if any. | 
## Example

```python
from lusid.models.partner_allocation_run_result import PartnerAllocationRunResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: ResourceId = # Replace with your value
period_start: datetime = # Replace with your value
period_end: datetime = # Replace with your value
nav_type_code: StrictStr = "example_nav_type_code"
status: StrictStr = "example_status"
run_id: StrictStr = "example_run_id"
pools: List[PartnerAllocationPool] = # Replace with your value
unattributed: List[UnattributedAmount] = # Replace with your value
booked_transaction_ids: List[StrictStr] = # Replace with your value
partner_allocation_run_result_instance = PartnerAllocationRunResult(fund_id=fund_id, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, status=status, run_id=run_id, pools=pools, unattributed=unattributed, booked_transaction_ids=booked_transaction_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

