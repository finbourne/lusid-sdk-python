# FieldDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**is_required** | **bool** |  | 
**is_unique** | **bool** |  | 
**value_type** | **str** |  | [optional] 
## Example

```python
from lusid.models.field_definition import FieldDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr, validator

key: StrictStr = "example_key"
is_required: StrictBool = # Replace with your value
is_required:StrictBool = True
is_unique: StrictBool = # Replace with your value
is_unique:StrictBool = True
value_type: Optional[StrictStr] = "example_value_type"
field_definition_instance = FieldDefinition(key=key, is_required=is_required, is_unique=is_unique, value_type=value_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

