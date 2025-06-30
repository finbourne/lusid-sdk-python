# CustomEntityFieldDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field. | 
**lifetime** | **str** | Describes how the field’s values can change over time. The available values are: “Perpetual”, “TimeVariant”. | 
**type** | **str** | The value type for the field. Available values are: “String”, “Boolean”, “DateTime”, “Decimal”. | 
**collection_type** | **str** | The collection type for the field. Available values are: “Single”, “Array”. Null value defaults to “Single” | [optional] 
**required** | **bool** | Whether the field is required or not. | 
**description** | **str** | An optional description for the field. | [optional] 
## Example

```python
from lusid.models.custom_entity_field_definition import CustomEntityFieldDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr

name: StrictStr = "example_name"
lifetime: StrictStr = "example_lifetime"
type: StrictStr = "example_type"
collection_type: Optional[StrictStr] = "example_collection_type"
required: StrictBool = # Replace with your value
required:StrictBool = True
description: Optional[StrictStr] = "example_description"
custom_entity_field_definition_instance = CustomEntityFieldDefinition(name=name, lifetime=lifetime, type=type, collection_type=collection_type, required=required, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

