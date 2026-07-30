# RecExceptionCountByResultType

Exception result counts broken down by result type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_break** | **int** | The number of Break results. | 
**partial_match** | **int** | The number of Partial Match results. | 
**partial_cross** | **int** | The number of Partial Cross results. | 
## Example

```python
from lusid.models.rec_exception_count_by_result_type import RecExceptionCountByResultType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_break: StrictInt = # Replace with your value
var_break: StrictInt = 42
partial_match: StrictInt = # Replace with your value
partial_match: StrictInt = 42
partial_cross: StrictInt = # Replace with your value
partial_cross: StrictInt = 42
rec_exception_count_by_result_type_instance = RecExceptionCountByResultType(var_break=var_break, partial_match=partial_match, partial_cross=partial_cross)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

