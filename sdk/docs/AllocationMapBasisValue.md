# AllocationMapBasisValue

The value one investor record is weighted by when an Allocation Map is resolved.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the basis value belongs to. | 
**basis_value** | **float** | The value the investor record is weighted by, for example its commitment. | 
## Example

```python
from lusid.models.allocation_map_basis_value import AllocationMapBasisValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
basis_value: Union[StrictFloat, StrictInt] = # Replace with your value
allocation_map_basis_value_instance = AllocationMapBasisValue(investor_record_id=investor_record_id, basis_value=basis_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

