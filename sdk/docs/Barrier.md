# Barrier

Barrier class for exotic FxOption
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Supported string (enumeration) values are: [Down, Up]. | 
**level** | **float** | Trigger level, which the underlying should (or should not) cross/touch. | 
**monitoring** | **str** | Supported string (enumeration) values are: [European, Bermudan, American].  Defaults to \&quot;European\&quot; if not set. | [optional] 
**type** | **str** | Supported string (enumeration) values are: [Knockin, Knockout]. | 
## Example

```python
from lusid.models.barrier import Barrier
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr

direction: StrictStr = "example_direction"
level: Union[StrictFloat, StrictInt] = # Replace with your value
monitoring: Optional[StrictStr] = "example_monitoring"
type: StrictStr = "example_type"
barrier_instance = Barrier(direction=direction, level=level, monitoring=monitoring, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

