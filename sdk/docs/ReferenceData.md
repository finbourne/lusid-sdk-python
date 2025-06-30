# ReferenceData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_definitions** | [**List[FieldDefinition]**](FieldDefinition.md) |  | 
**values** | [**List[FieldValue]**](FieldValue.md) |  | 
## Example

```python
from lusid.models.reference_data import ReferenceData
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

field_definitions: conlist(FieldDefinition) = # Replace with your value
values: conlist(FieldValue) = # Replace with your value
reference_data_instance = ReferenceData(field_definitions=field_definitions, values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

