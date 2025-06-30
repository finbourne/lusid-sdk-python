# CutLocalTime

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **int** |  | [optional] 
**minutes** | **int** |  | [optional] 
**seconds** | **float** |  | [optional] 
## Example

```python
from lusid.models.cut_local_time import CutLocalTime
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, StrictFloat, StrictInt

hours: Optional[StrictInt] = None
hours: Optional[StrictInt] = None
minutes: Optional[StrictInt] = None
minutes: Optional[StrictInt] = None
seconds: Optional[Union[StrictFloat, StrictInt]] = None
cut_local_time_instance = CutLocalTime(hours=hours, minutes=minutes, seconds=seconds)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

