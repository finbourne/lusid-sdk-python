# RecResultStreak

The run of consecutive instances, ending at this result, in which the same result was produced, with its  difference and open sub-streaks.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predecessor** | [**RecResultStreakPredecessor**](RecResultStreakPredecessor.md) |  | 
**age** | **str** | The ISO 8601 duration from the startResult&#39;s asAtFirstSeen to the runAsAt of this result&#39;s latest run. Always positive. | 
**count_instances** | **int** | The number of instances in the streak, including this one. Always 2 or more. | 
**start_result** | [**RecAgedResult**](RecAgedResult.md) |  | 
**difference_streak** | [**RecResultSubStreak**](RecResultSubStreak.md) |  | 
**open_streak** | [**RecResultSubStreak**](RecResultSubStreak.md) |  | 
## Example

```python
from lusid.models.rec_result_streak import RecResultStreak
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

predecessor: RecResultStreakPredecessor
age: StrictStr = "example_age"
count_instances: StrictInt = # Replace with your value
count_instances: StrictInt = 42
start_result: RecAgedResult = # Replace with your value
difference_streak: RecResultSubStreak = # Replace with your value
open_streak: RecResultSubStreak = # Replace with your value
rec_result_streak_instance = RecResultStreak(predecessor=predecessor, age=age, count_instances=count_instances, start_result=start_result, difference_streak=difference_streak, open_streak=open_streak)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

