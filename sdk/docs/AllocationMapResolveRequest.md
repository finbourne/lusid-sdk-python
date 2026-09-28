# AllocationMapResolveRequest

A dry run of an Allocation Map: the event to share, and the basis values to share it by.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The kind of allocation event to resolve: CapitalCall, Distribution, FeeExpense or ValuationMove. The map must define a basis for it. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. | 
**amount** | **float** | The amount of the event to share between the participants, in the event currency. | 
**currency** | **str** | The currency of the amount. | 
**basis_values** | [**List[AllocationMapBasisValue]**](AllocationMapBasisValue.md) | For a ValueWeighted or PropertyWeighted basis, the basis value of each participating investor record, supplied by the caller until investor records are read from LUSID. Under the AllCommittedToMembers rule these also name the committed investor records. Not needed for a FixedPercentage basis. | [optional] 
## Example

```python
from lusid.models.allocation_map_resolve_request import AllocationMapResolveRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

event_type: StrictStr = "example_event_type"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
basis_values: Optional[List[AllocationMapBasisValue]] = # Replace with your value
allocation_map_resolve_request_instance = AllocationMapResolveRequest(event_type=event_type, amount=amount, currency=currency, basis_values=basis_values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

