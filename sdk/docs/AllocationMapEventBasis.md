# AllocationMapEventBasis

The basis an Allocation Map applies to one kind of allocation event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The kind of allocation event the basis applies to: CapitalCall, Distribution, FeeExpense or ValuationMove. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. | 
**basis** | [**AllocationMapBasis**](AllocationMapBasis.md) |  | 
## Example

```python
from lusid.models.allocation_map_event_basis import AllocationMapEventBasis
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

event_type: StrictStr = "example_event_type"
basis: AllocationMapBasis
allocation_map_event_basis_instance = AllocationMapEventBasis(event_type=event_type, basis=basis)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

