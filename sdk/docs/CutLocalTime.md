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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

hours: Optional[StrictInt] = None
hours: Optional[StrictInt] = None
minutes: Optional[StrictInt] = None
minutes: Optional[StrictInt] = None
seconds: Optional[Union[StrictFloat, StrictInt]] = None
cut_local_time_instance = CutLocalTime(hours=hours, minutes=minutes, seconds=seconds)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

