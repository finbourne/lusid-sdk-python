# ScopeDefinition

A list of scopes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The unique identifier for the scope. | 
## Example

```python
from lusid.models.scope_definition import ScopeDefinition
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

scope: StrictStr = "example_scope"
scope_definition_instance = ScopeDefinition(scope=scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

