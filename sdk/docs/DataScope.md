# DataScope

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**Client**](Client.md) |  | [optional] 
**scope** | **str** |  | [optional] 
## Example

```python
from lusid.models.data_scope import DataScope
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictStr

client: Optional[Client] = None
scope: Optional[StrictStr] = "example_scope"
data_scope_instance = DataScope(client=client, scope=scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

