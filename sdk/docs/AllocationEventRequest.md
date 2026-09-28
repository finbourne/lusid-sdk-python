# AllocationEventRequest

The request used to raise or replace an Allocation Event. The event is computed against its map straight away.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Allocation Event. Together with the scope this uniquely identifies the event. | 
**allocation_map_id** | [**ResourceId**](ResourceId.md) |  | 
**event_type** | **str** | The type of the event: CapitalCall, Distribution, FeeExpense or ValuationMove. Selects the basis rule from the map. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. | 
**amount** | **float** | The total amount to be shared across the participants. | 
**currency** | **str** | The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places. | 
**event_date** | **datetime** | The date of the event: the point at which the map, its participants and their basis values are read. | 
**description** | **str** | A description of the Allocation Event. | [optional] 
**basis_values** | [**List[AllocationMapBasisValue]**](AllocationMapBasisValue.md) | Optional basis values per investor record, used when the map&#39;s basis is not resolvable from stored data. | [optional] 
**effective_at** | **datetime** | The effective datetime at which the event is created or replaced. Defaults to the earliest effective time on create and the current LUSID system datetime on replace. | [optional] 
## Example

```python
from lusid.models.allocation_event_request import AllocationEventRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
allocation_map_id: ResourceId = # Replace with your value
event_type: StrictStr = "example_event_type"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
event_date: datetime = # Replace with your value
description: Optional[StrictStr] = "example_description"
basis_values: Optional[List[AllocationMapBasisValue]] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
allocation_event_request_instance = AllocationEventRequest(code=code, allocation_map_id=allocation_map_id, event_type=event_type, amount=amount, currency=currency, event_date=event_date, description=description, basis_values=basis_values, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

