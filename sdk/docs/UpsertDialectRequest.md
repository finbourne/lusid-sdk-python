# UpsertDialectRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**DialectId**](DialectId.md) |  | 
**var_schema** | [**DialectSchema**](DialectSchema.md) |  | 
## Example

```python
from lusid.models.upsert_dialect_request import UpsertDialectRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

id: DialectId = # Replace with your value
var_schema: DialectSchema = # Replace with your value
upsert_dialect_request_instance = UpsertDialectRequest(id=id, var_schema=var_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

