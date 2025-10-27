# CreateDataMapRequest

Request to create a new data map
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**DataMapKey**](DataMapKey.md) |  | 
**data** | [**DataMapping**](DataMapping.md) |  | [optional] 
## Example

```python
from lusid.models.create_data_map_request import CreateDataMapRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: DataMapKey
data: Optional[DataMapping] = None
create_data_map_request_instance = CreateDataMapRequest(id=id, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

