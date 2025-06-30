# AccessMetadataOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AccessMetadataValue]**](AccessMetadataValue.md) |  | 
**path** | **str** |  | 
**op** | **str** | The available values are: add, remove | 
**var_from** | **str** |  | [optional] 
## Example

```python
from lusid.models.access_metadata_operation import AccessMetadataOperation
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

value: conlist(AccessMetadataValue, min_items=1) = Field(...)
path: StrictStr = "example_path"
op: StrictStr = "example_op"
var_from: Optional[StrictStr] = "example_var_from"
access_metadata_operation_instance = AccessMetadataOperation(value=value, path=path, op=op, var_from=var_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

