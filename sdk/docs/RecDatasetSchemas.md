# RecDatasetSchemas

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**RecDatasetSchema**](RecDatasetSchema.md) |  | [optional] 
**right** | [**RecDatasetSchema**](RecDatasetSchema.md) |  | [optional] 
## Example

```python
from lusid.models.rec_dataset_schemas import RecDatasetSchemas
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: Optional[RecDatasetSchema] = None
right: Optional[RecDatasetSchema] = None
rec_dataset_schemas_instance = RecDatasetSchemas(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

