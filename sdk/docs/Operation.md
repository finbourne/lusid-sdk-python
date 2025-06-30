# Operation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | [optional] 
**path** | **str** |  | 
**op** | **str** |  | 
**var_from** | **str** |  | [optional] 
## Example

```python
from lusid.models.operation import Operation
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

value: Optional[Any] = None
path: StrictStr = "example_path"
op: StrictStr = "example_op"
var_from: Optional[StrictStr] = "example_var_from"
operation_instance = Operation(value=value, path=path, op=op, var_from=var_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

