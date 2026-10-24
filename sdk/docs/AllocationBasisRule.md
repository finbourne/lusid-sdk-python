# AllocationBasisRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character** | **str** |  | 
**basis** | **str** | Available values: CommittedCapital, PaidInCapital, DealPaidIn. | 
## Example

```python
from lusid.models.allocation_basis_rule import AllocationBasisRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

character: StrictStr = "example_character"
basis: StrictStr = "example_basis"
allocation_basis_rule_instance = AllocationBasisRule(character=character, basis=basis)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

