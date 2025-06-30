# Client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
## Example

```python
from lusid.models.client import Client
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictStr

name: Optional[StrictStr] = "example_name"
client_instance = Client(name=name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

