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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

id: DataMapKey = # Replace with your value
data: Optional[DataMapping] = None
create_data_map_request_instance = CreateDataMapRequest(id=id, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

