# CustomDataModelPropertySpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The property key that is required/allowed on the bound entity. | 
**required** | **bool** | Whether property is required or allowed. | [optional] 
## Example

```python
from lusid.models.custom_data_model_property_specification import CustomDataModelPropertySpecification
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_key: StrictStr = "example_property_key"
required: Optional[StrictBool] = # Replace with your value
required:Optional[StrictBool] = None
custom_data_model_property_specification_instance = CustomDataModelPropertySpecification(property_key=property_key, required=required)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

