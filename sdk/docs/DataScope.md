# DataScope

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**Client**](Client.md) |  | [optional] 
**scope** | **str** |  | [optional] 
## Example

```python
from lusid.models.data_scope import DataScope
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

client: Optional[Client] = None
scope: Optional[StrictStr] = "example_scope"
data_scope_instance = DataScope(client=client, scope=scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

