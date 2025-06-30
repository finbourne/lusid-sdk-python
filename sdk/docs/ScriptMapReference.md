# ScriptMapReference

Provides information about the location of a script map within the configuration store
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the configuration store entry where the translation map is located. | 
**code** | **str** | The code of the configuration store entry where the translation map is located. | 
**key** | **str** | The key of the configuration store entry where the translation map is located. | 
## Example

```python
from lusid.models.script_map_reference import ScriptMapReference
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
key: StrictStr = "example_key"
script_map_reference_instance = ScriptMapReference(scope=scope, code=code, key=key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

