# BreakCodeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.break_code_source import BreakCodeSource
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

data_type_id: ResourceId = # Replace with your value
break_code_source_instance = BreakCodeSource(data_type_id=data_type_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

