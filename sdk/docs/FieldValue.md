# FieldValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**fields** | **Dict[str, Optional[str]]** |  | [optional] 
**numeric_fields** | **Dict[str, float]** |  | [optional] 
## Example

```python
from lusid.models.field_value import FieldValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: StrictStr = "example_value"
fields: Optional[Dict[str, Optional[StrictStr]]] = None
numeric_fields: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
field_value_instance = FieldValue(value=value, fields=fields, numeric_fields=numeric_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

