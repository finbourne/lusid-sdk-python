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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: List[AccessMetadataValue]
path: StrictStr = "example_path"
op: StrictStr = "example_op"
var_from: Optional[StrictStr] = "example_var_from"
access_metadata_operation_instance = AccessMetadataOperation(value=value, path=path, op=op, var_from=var_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

