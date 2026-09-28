# AllocationMapBasis

How an allocation event is weighted between the participants of an Allocation Map.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | How the event is weighted between the participants. ValueWeighted apportions pro rata to each participant&#39;s value; PropertyWeighted apportions pro rata to the property named in &#39;property&#39;; FixedPercentage apportions by the factors in fixedFactors. Available values: ValueWeighted, PropertyWeighted, FixedPercentage. | [optional] 
**var_property** | [**ApportionmentMethodProperty**](ApportionmentMethodProperty.md) |  | [optional] 
**fixed_factors** | [**List[AllocationMapFixedFactor]**](AllocationMapFixedFactor.md) | For a FixedPercentage basis, the share of the amount each participating investor record takes. At least one is required under that kind, every factor must be positive, and the factors must sum to 1. | [optional] 
**scoped_to_member** | **bool** | Whether the basis is evaluated only over amounts booked against the structure member rather than fund-wide. | [optional] 
## Example

```python
from lusid.models.allocation_map_basis import AllocationMapBasis
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

kind: Optional[StrictStr] = "example_kind"
var_property: Optional[ApportionmentMethodProperty] = # Replace with your value
fixed_factors: Optional[List[AllocationMapFixedFactor]] = # Replace with your value
scoped_to_member: Optional[StrictBool] = # Replace with your value
scoped_to_member:Optional[StrictBool] = None
allocation_map_basis_instance = AllocationMapBasis(kind=kind, var_property=var_property, fixed_factors=fixed_factors, scoped_to_member=scoped_to_member)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

