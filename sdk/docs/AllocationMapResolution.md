# AllocationMapResolution

The result of resolving an Allocation Map for one event: how much each investor record receives, and why.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The kind of allocation event that was resolved. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. | [optional] 
**amount** | **float** | The amount that was shared. | [optional] 
**currency** | **str** | The currency of the amount. | [optional] 
**basis_rule** | **str** | The basis the map applies to this event type. Available values: ValueWeighted, PropertyWeighted, FixedPercentage. | [optional] 
**basis_pool** | **float** | The sum of the basis values over the participants that share the remainder pro rata. | [optional] 
**fixed_total** | **float** | The total taken off the top by FixedPercentage exceptions before the remainder is shared. | [optional] 
**participant_count** | **int** | The number of investor records that receive a share, whether fixed or pro rata. | [optional] 
**excluded_count** | **int** | The number of investor records an exception removed from the allocation. | [optional] 
**allocations** | [**List[AllocationMapAllocation]**](AllocationMapAllocation.md) | The share of each investor record, including those excluded, which receive nothing. | [optional] 
**reconciles** | **bool** | Whether the allocated amounts sum exactly to the requested amount. Amounts are rounded to two decimal places with the largest-remainder method, so an amount with more decimal places does not reconcile. | [optional] 
## Example

```python
from lusid.models.allocation_map_resolution import AllocationMapResolution
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

event_type: Optional[StrictStr] = "example_event_type"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
basis_rule: Optional[StrictStr] = "example_basis_rule"
basis_pool: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fixed_total: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
participant_count: Optional[StrictInt] = # Replace with your value
participant_count: Optional[StrictInt] = None
excluded_count: Optional[StrictInt] = # Replace with your value
excluded_count: Optional[StrictInt] = None
allocations: Optional[List[AllocationMapAllocation]] = # Replace with your value
reconciles: Optional[StrictBool] = # Replace with your value
reconciles:Optional[StrictBool] = None
allocation_map_resolution_instance = AllocationMapResolution(event_type=event_type, amount=amount, currency=currency, basis_rule=basis_rule, basis_pool=basis_pool, fixed_total=fixed_total, participant_count=participant_count, excluded_count=excluded_count, allocations=allocations, reconciles=reconciles)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

