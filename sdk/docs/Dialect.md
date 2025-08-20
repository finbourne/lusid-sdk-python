# Dialect

The language/format of a translatable entity. Entities can be LUSID native or external and the Dialect describes 1) the system that understands the entity and 2) applicable validation for the entity, in the form of a schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**DialectId**](DialectId.md) |  | 
**var_schema** | [**DialectSchema**](DialectSchema.md) |  | 
**version** | [**Version**](Version.md) |  | [optional] 
## Example

```python
from lusid.models.dialect import Dialect
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

id: DialectId = # Replace with your value
var_schema: DialectSchema = # Replace with your value
version: Optional[Version] = None
dialect_instance = Dialect(id=id, var_schema=var_schema, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

