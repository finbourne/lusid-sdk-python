# CustomDataModelIdentifierTypeSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_key** | **str** | The identifier type that is required/allowed on the bound entity. | 
**required** | **bool** | Whether identifier type is required or allowed. | [optional] 
## Example

```python
from lusid.models.custom_data_model_identifier_type_specification import CustomDataModelIdentifierTypeSpecification
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

identifier_key: StrictStr = "example_identifier_key"
required: Optional[StrictBool] = # Replace with your value
required:Optional[StrictBool] = None
custom_data_model_identifier_type_specification_instance = CustomDataModelIdentifierTypeSpecification(identifier_key=identifier_key, required=required)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

