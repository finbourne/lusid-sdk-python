# RecResultSubStreak

The part of a streak, ending at this result, over which a stricter condition held: same difference, or open.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **str** | The ISO 8601 duration from the startResult&#39;s asAtFirstSeen to the runAsAt of this result&#39;s latest run. Zero when the predecessor does not extend the sub-streak. | 
**count_instances** | **int** | The number of instances in the sub-streak, including this one. Null when the predecessor does not extend the sub-streak; otherwise 2 or more. | [optional] 
**start_result** | [**RecAgedResult**](RecAgedResult.md) |  | [optional] 
## Example

```python
from lusid.models.rec_result_sub_streak import RecResultSubStreak
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

age: StrictStr = "example_age"
count_instances: Optional[StrictInt] = # Replace with your value
count_instances: Optional[StrictInt] = None
start_result: Optional[RecAgedResult] = # Replace with your value
rec_result_sub_streak_instance = RecResultSubStreak(age=age, count_instances=count_instances, start_result=start_result)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

