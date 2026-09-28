# AllocationMapAllocation

One investor record's share of a resolved allocation event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record that receives the share. | [optional] 
**basis_value** | **float** | The basis value the pro rata share was weighted by. Absent for a fixed or excluded investor record. | [optional] 
**weight** | **float** | The fraction of the remainder the investor record receives, or the fixed fraction of the whole amount for a FixedPercentage exception. | [optional] 
**amount** | **float** | The amount allocated to the investor record. | [optional] 
**treatment** | **str** | How the share was found. Derived means pro rata from the basis; FixedPercentage means off the top from an exception; Excluded means an exception removed the investor record and it receives nothing. Available values: Derived, FixedPercentage, Excluded. | [optional] 
## Example

```python
from lusid.models.allocation_map_allocation import AllocationMapAllocation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: Optional[StrictStr] = "example_investor_record_id"
basis_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
weight: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
treatment: Optional[StrictStr] = "example_treatment"
allocation_map_allocation_instance = AllocationMapAllocation(investor_record_id=investor_record_id, basis_value=basis_value, weight=weight, amount=amount, treatment=treatment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

