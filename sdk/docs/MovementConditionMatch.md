# MovementConditionMatch

The outcome of one movement's condition for a transaction. Reported per movement rather than keyed by  movement, because a transaction type may configure several movements that share a side and have no name.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movement_name** | **str** | The name of the movement, or null if the movement is unnamed. | [optional] 
**side** | **str** | The side the movement is configured against. | 
**condition_matched** | **bool** | Whether the movement&#39;s condition was satisfied by this transaction. A movement with no condition always matches. | [optional] 
## Example

```python
from lusid.models.movement_condition_match import MovementConditionMatch
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

movement_name: Optional[StrictStr] = "example_movement_name"
side: StrictStr = "example_side"
condition_matched: Optional[StrictBool] = # Replace with your value
condition_matched:Optional[StrictBool] = None
movement_condition_match_instance = MovementConditionMatch(movement_name=movement_name, side=side, condition_matched=condition_matched)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

