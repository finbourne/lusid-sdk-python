# ReferenceData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_definitions** | [**List[FieldDefinition]**](FieldDefinition.md) |  | 
**values** | [**List[FieldValue]**](FieldValue.md) |  | 
## Example

```python
from lusid.models.reference_data import ReferenceData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

field_definitions: List[FieldDefinition] = # Replace with your value
values: List[FieldValue]
reference_data_instance = ReferenceData(field_definitions=field_definitions, values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

