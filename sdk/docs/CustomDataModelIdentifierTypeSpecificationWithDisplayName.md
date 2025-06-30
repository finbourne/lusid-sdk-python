# CustomDataModelIdentifierTypeSpecificationWithDisplayName

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the property definition. | [optional] 
**identifier_key** | **str** | The identifier type that is required/allowed on the bound entity. | 
**required** | **bool** | Whether identifier type is required or allowed. | [optional] 
**identifier_type** | **str** | The name of the identifier type. | [optional] 
## Example

```python
from lusid.models.custom_data_model_identifier_type_specification_with_display_name import CustomDataModelIdentifierTypeSpecificationWithDisplayName
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

display_name: Optional[StrictStr] = "example_display_name"
identifier_key: StrictStr = "example_identifier_key"
required: Optional[StrictBool] = # Replace with your value
required:Optional[StrictBool] = None
identifier_type: Optional[StrictStr] = "example_identifier_type"
custom_data_model_identifier_type_specification_with_display_name_instance = CustomDataModelIdentifierTypeSpecificationWithDisplayName(display_name=display_name, identifier_key=identifier_key, required=required, identifier_type=identifier_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

