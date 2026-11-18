# PartnerAllocation

One partner's share of an allocation pool.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the allocation belongs to. | 
**basis_weight** | **float** | The partner&#39;s weight in the pool&#39;s basis. | 
**amount** | **float** | The amount allocated to the partner. | 
**reason** | **str** | Why a partner listed at 0.00 took no share of the pool. Available values: Excluded (the bucket&#39;s rule leaves the partner out), Exempt (the partner&#39;s register flag sits it out), ZeroBasis (the partner has nothing on the pool&#39;s basis). Absent on a partner that shares; a partner at 0.00 with no reason shares the pool, but its share rounded to nothing at the pool&#39;s scale. | [optional] 
## Example

```python
from lusid.models.partner_allocation import PartnerAllocation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
basis_weight: Union[StrictFloat, StrictInt] = # Replace with your value
amount: Union[StrictFloat, StrictInt] = # Replace with your value
reason: Optional[StrictStr] = "example_reason"
partner_allocation_instance = PartnerAllocation(investor_record_id=investor_record_id, basis_weight=basis_weight, amount=amount, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

