# ResourceId

Identifiers of an entity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope used to identify an entity | 
**code** | **str** | The code used to identify an entity | 
## Example

```python
from lusid.models.resource_id import ResourceId
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
resource_id_instance = ResourceId(scope=scope, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

