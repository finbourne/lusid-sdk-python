# CustomDataModelIdentifierTypeSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_key** | **str** | The identifier type that is required/allowed on the bound entity. | 
**required** | **bool** | Whether identifier type is required or allowed. | [optional] 
## Example

```python
from lusid.models.custom_data_model_identifier_type_specification import CustomDataModelIdentifierTypeSpecification
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

identifier_key: StrictStr = "example_identifier_key"
required: Optional[StrictBool] = # Replace with your value
required:Optional[StrictBool] = None
custom_data_model_identifier_type_specification_instance = CustomDataModelIdentifierTypeSpecification(identifier_key=identifier_key, required=required)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

