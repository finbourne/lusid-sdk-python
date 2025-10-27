# RelationalDataPointFieldValueResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | The value of the field. | 
## Example

```python
from lusid.models.relational_data_point_field_value_response import RelationalDataPointFieldValueResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: Optional[Any] = # Replace with your value
relational_data_point_field_value_response_instance = RelationalDataPointFieldValueResponse(value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

