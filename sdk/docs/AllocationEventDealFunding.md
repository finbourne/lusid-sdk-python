# AllocationEventDealFunding

The details of a DealFunding Allocation Event: the deal the vehicle funds, where the money came from and which  investor records are excused from it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_id** | **str** | The deal the vehicle funds. A later capital call names it in an Investment row of its use of proceeds. | 
**facility_id** | **str** | The subscription facility the funding was drawn from. Absent means the deal was paid from cash. | [optional] 
**excluded_investor_record_ids** | **List[str]** | The investor records excused from the deal. They pay nothing towards it when it is called and the others take up their share. | [optional] 
## Example

```python
from lusid.models.allocation_event_deal_funding import AllocationEventDealFunding
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

deal_id: StrictStr = "example_deal_id"
facility_id: Optional[StrictStr] = "example_facility_id"
excluded_investor_record_ids: Optional[List[StrictStr]] = # Replace with your value
allocation_event_deal_funding_instance = AllocationEventDealFunding(deal_id=deal_id, facility_id=facility_id, excluded_investor_record_ids=excluded_investor_record_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

