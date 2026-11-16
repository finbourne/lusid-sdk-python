# RecResultStreakPredecessor

The same result in the previous instance, and which streaks it extends.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**RecAgedResult**](RecAgedResult.md) |  | 
**streak_types** | **List[str]** | Which streaks the predecessor extends: always Core, and Difference if the aggregate rule differences are unchanged. Open is not set yet. Available values: Core, Difference, Open. | 
## Example

```python
from lusid.models.rec_result_streak_predecessor import RecResultStreakPredecessor
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

result: RecAgedResult
streak_types: List[StrictStr] = # Replace with your value
rec_result_streak_predecessor_instance = RecResultStreakPredecessor(result=result, streak_types=streak_types)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

