# EntityIdentifier

Dto to expose mapped keys to new standardised format
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_scope** | **str** | The scope of the identifier | [optional] 
**identifier_type** | **str** | The type of the identifier | 
**identifier_value** | **str** | The value of the identifier | 
## Example

```python
from lusid.models.entity_identifier import EntityIdentifier
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

identifier_scope: Optional[StrictStr] = "example_identifier_scope"
identifier_type: StrictStr = "example_identifier_type"
identifier_value: StrictStr = "example_identifier_value"
entity_identifier_instance = EntityIdentifier(identifier_scope=identifier_scope, identifier_type=identifier_type, identifier_value=identifier_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

