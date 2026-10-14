# PartnerAllocationPool

One pool of an allocation run: an amount of a given character, split across the partners on a basis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character** | **str** | The character of the pool&#39;s amount, for example Income, RealisedGain or Expense. | 
**origin_member_short_code** | **str** | For a deal-linked pool, the short code of the member fund the amount originates from. | [optional] 
**pool_amount** | **float** | The amount in the pool. | 
**basis** | **str** | The basis the pool was shared on. Available values: CommittedCapital, PaidInCapital, DealPaidIn. | 
**allocations** | [**List[PartnerAllocation]**](PartnerAllocation.md) | Each partner&#39;s share of the pool. | 
**residual** | **float** | The rounding residual, carried by the largest allocation. | 
## Example

```python
from lusid.models.partner_allocation_pool import PartnerAllocationPool
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

character: StrictStr = "example_character"
origin_member_short_code: Optional[StrictStr] = "example_origin_member_short_code"
pool_amount: Union[StrictFloat, StrictInt] = # Replace with your value
basis: StrictStr = "example_basis"
allocations: List[PartnerAllocation] = # Replace with your value
residual: Union[StrictFloat, StrictInt] = # Replace with your value
partner_allocation_pool_instance = PartnerAllocationPool(character=character, origin_member_short_code=origin_member_short_code, pool_amount=pool_amount, basis=basis, allocations=allocations, residual=residual)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

