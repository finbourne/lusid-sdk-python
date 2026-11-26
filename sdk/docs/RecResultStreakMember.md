# RecResultStreakMember

A member of a result's streak, tagged relative to the requested result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**RecResult**](RecResult.md) |  | 
**streak_types** | **List[str]** | Which streaks the member shares with the requested result: always Core; Difference when every link between them has unchanged aggregate rule differences; Open when it, the requested result and every member between them have an open exception. The requested result is always Difference. Available values: Core, Difference, Open. | 
**relation** | **str** | Where the member sits relative to the requested result: Predecessor in an earlier instance, Requested for the result itself, Successor in a later instance. Available values: Predecessor, Requested, Successor. | 
## Example

```python
from lusid.models.rec_result_streak_member import RecResultStreakMember
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

result: RecResult
streak_types: List[StrictStr] = # Replace with your value
relation: StrictStr = "example_relation"
rec_result_streak_member_instance = RecResultStreakMember(result=result, streak_types=streak_types, relation=relation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

