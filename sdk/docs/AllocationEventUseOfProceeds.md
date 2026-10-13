# AllocationEventUseOfProceeds

One row of a CapitalCall Allocation Event's use of proceeds: what part of the call pays for what.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | **str** | What the row pays for: Investment, FacilityRepayment, FacilityInterest, ManagementFee or Expenses. Available values: Investment, FacilityRepayment, FacilityInterest, ManagementFee, Expenses. | 
**deal_id** | **str** | The deal the row funds, or whose facility draw it repays. Required for an Investment row. | [optional] 
**amount** | **float** | The part of the call the row takes, in the event currency. Greater than zero. | 
**facility_id** | **str** | The facility the row repays. Required for a FacilityRepayment row; on an Investment row it is filled in from the deal&#39;s funding when the call is computed. | [optional] 
## Example

```python
from lusid.models.allocation_event_use_of_proceeds import AllocationEventUseOfProceeds
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

purpose: StrictStr = "example_purpose"
deal_id: Optional[StrictStr] = "example_deal_id"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
facility_id: Optional[StrictStr] = "example_facility_id"
allocation_event_use_of_proceeds_instance = AllocationEventUseOfProceeds(purpose=purpose, deal_id=deal_id, amount=amount, facility_id=facility_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

