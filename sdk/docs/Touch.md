# Touch

Touch class for exotic FxOption
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Supported string (enumeration) values are: [Down, Up]. | 
**level** | **float** | Trigger level, which the underlying should (or should not) cross/touch. | 
**monitoring** | **str** | Supported string (enumeration) values are: [European, Bermudan, American].  Defaults to \&quot;European\&quot; if not set. | [optional] 
**type** | **str** | Supported string (enumeration) values are: [Touch, Notouch]. | 
## Example

```python
from lusid.models.touch import Touch
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

direction: StrictStr = "example_direction"
level: Union[StrictFloat, StrictInt] = # Replace with your value
monitoring: Optional[StrictStr] = "example_monitoring"
type: StrictStr = "example_type"
touch_instance = Touch(direction=direction, level=level, monitoring=monitoring, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

