# FundStructureAllocationBasis

The default apportionment basis of a Fund Structure member.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | How the apportionment is weighted. ValueWeighted apportions pro rata to each investing member&#39;s value; PropertyWeighted apportions pro rata to the property named in &#39;property&#39;; FixedPercentage defers to factors held on an allocation map. A ValueWeighted basis is rejected where a holder of this member also holds an unrelated member, because the member could not be finalised before that sibling is valued. Available values: ValueWeighted, PropertyWeighted, FixedPercentage. | [optional] 
**var_property** | [**ApportionmentMethodProperty**](ApportionmentMethodProperty.md) |  | [optional] 
**scoped_to_member** | **bool** | Whether the basis is evaluated only over amounts booked against this member rather than fund-wide. | [optional] 
## Example

```python
from lusid.models.fund_structure_allocation_basis import FundStructureAllocationBasis
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

kind: Optional[StrictStr] = "example_kind"
var_property: Optional[ApportionmentMethodProperty] = # Replace with your value
scoped_to_member: Optional[StrictBool] = # Replace with your value
scoped_to_member:Optional[StrictBool] = None
fund_structure_allocation_basis_instance = FundStructureAllocationBasis(kind=kind, var_property=var_property, scoped_to_member=scoped_to_member)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

