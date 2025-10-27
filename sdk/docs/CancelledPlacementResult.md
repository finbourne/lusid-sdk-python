# CancelledPlacementResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_state** | [**Placement**](Placement.md) |  | [optional] 
**cancelled_child_placements** | [**List[ResourceId]**](ResourceId.md) | Child placements which have also been cancelled following cancellation of the parent | 
## Example

```python
from lusid.models.cancelled_placement_result import CancelledPlacementResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

placement_state: Optional[Placement] = # Replace with your value
cancelled_child_placements: List[ResourceId] = # Replace with your value
cancelled_placement_result_instance = CancelledPlacementResult(placement_state=placement_state, cancelled_child_placements=cancelled_child_placements)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

