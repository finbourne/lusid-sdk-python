# PartnerAllocationRunRequest

The request to allocate a period's income summary to the partners of a partnership fund.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** | The start of the period to allocate, exclusive. | 
**period_end** | **datetime** | The end of the period to allocate, inclusive. A valuation point must end on this date. | 
**nav_type_code** | **str** | The NAV type to allocate under. Defaults to the fund&#39;s primary NAV type. | [optional] 
**dry_run** | **bool** | When true, the allocation is computed and returned but nothing is booked. | [optional] 
**correction** | **bool** | When true, a period that has already been allocated may be re-allocated. | [optional] 
## Example

```python
from lusid.models.partner_allocation_run_request import PartnerAllocationRunRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

period_start: datetime = # Replace with your value
period_end: datetime = # Replace with your value
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
dry_run: Optional[StrictBool] = # Replace with your value
dry_run:Optional[StrictBool] = None
correction: Optional[StrictBool] = # Replace with your value
correction:Optional[StrictBool] = None
partner_allocation_run_request_instance = PartnerAllocationRunRequest(period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, dry_run=dry_run, correction=correction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

