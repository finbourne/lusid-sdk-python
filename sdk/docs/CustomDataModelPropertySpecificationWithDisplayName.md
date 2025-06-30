# CustomDataModelPropertySpecificationWithDisplayName

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the property definition. | [optional] 
**property_key** | **str** | The property key that is required/allowed on the bound entity. | 
**required** | **bool** | Whether property is required or allowed. | [optional] 
## Example

```python
from lusid.models.custom_data_model_property_specification_with_display_name import CustomDataModelPropertySpecificationWithDisplayName
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

display_name: Optional[StrictStr] = "example_display_name"
property_key: StrictStr = "example_property_key"
required: Optional[StrictBool] = # Replace with your value
required:Optional[StrictBool] = None
custom_data_model_property_specification_with_display_name_instance = CustomDataModelPropertySpecificationWithDisplayName(display_name=display_name, property_key=property_key, required=required)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

