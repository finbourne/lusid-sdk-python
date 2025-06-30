# User

The unique id of the user that issued the command.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the user. | [optional] 
## Example

```python
from lusid.models.user import User
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

id: Optional[StrictStr] = "example_id"
user_instance = User(id=id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

