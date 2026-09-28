# AllocationMapFixedFactor

The weight of one investor record under a FixedPercentage basis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the factor belongs to. | 
**factor** | **float** | The weight of the investor record. Weights are normalised over the participants that receive the remainder, so they need not sum to 1. | 
## Example

```python
from lusid.models.allocation_map_fixed_factor import AllocationMapFixedFactor
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
factor: Union[StrictFloat, StrictInt] = # Replace with your value
allocation_map_fixed_factor_instance = AllocationMapFixedFactor(investor_record_id=investor_record_id, factor=factor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

