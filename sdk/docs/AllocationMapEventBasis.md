# AllocationMapEventBasis

The basis an Allocation Map applies to one kind of allocation event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The kind of allocation event the basis applies to: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default, Commitment or DealFunding. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding. | 
**basis** | [**AllocationMapBasis**](AllocationMapBasis.md) |  | 
**component** | **str** | The component of the event the basis applies to, for example MgmtFee or OrgCost. Absent means the entry is the default for every component of the event type without an entry of its own. | [optional] 
## Example

```python
from lusid.models.allocation_map_event_basis import AllocationMapEventBasis
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

event_type: StrictStr = "example_event_type"
basis: AllocationMapBasis
component: Optional[StrictStr] = "example_component"
allocation_map_event_basis_instance = AllocationMapEventBasis(event_type=event_type, basis=basis, component=component)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

