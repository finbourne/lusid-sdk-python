# FieldValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**fields** | **Dict[str, str]** |  | [optional] 
**numeric_fields** | **Dict[str, float]** |  | [optional] 
## Example

```python
from lusid.models.field_value import FieldValue
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr, validator

value: StrictStr = "example_value"
fields: Optional[Dict[str, StrictStr]] = None
numeric_fields: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
field_value_instance = FieldValue(value=value, fields=fields, numeric_fields=numeric_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

