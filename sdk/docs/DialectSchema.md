# DialectSchema

A schema that a given document must obey. A representation of the validation of a particular Dialect,  in a given language.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of schema this represents | 
**body** | **str** | The body of the schema | [optional] 
## Example

```python
from lusid.models.dialect_schema import DialectSchema
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

type: StrictStr = "example_type"
body: Optional[StrictStr] = "example_body"
dialect_schema_instance = DialectSchema(type=type, body=body)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

