# RelationalDatasetFieldDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The unique identifier for the field within the dataset. | 
**display_name** | **str** | A user-friendly display name for the field. | [optional] 
**description** | **str** | A detailed description of the field and its purpose. | [optional] 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**required** | **bool** | Whether this field is mandatory in the dataset. | [optional] 
**usage** | **str** | The intended usage of the field (SeriesIdentifier, Value, or Metadata). | 
## Example

```python
from lusid.models.relational_dataset_field_definition import RelationalDatasetFieldDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr

field_name: StrictStr = "example_field_name"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
data_type_id: ResourceId = # Replace with your value
required: Optional[StrictBool] = # Replace with your value
required:Optional[StrictBool] = None
usage: StrictStr = "example_usage"
relational_dataset_field_definition_instance = RelationalDatasetFieldDefinition(field_name=field_name, display_name=display_name, description=description, data_type_id=data_type_id, required=required, usage=usage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

