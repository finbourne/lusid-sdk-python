# ErrorDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the failed item that this error relates to. | [optional] 
**type** | **str** | The type of failure that occurred. | [optional] 
**detail** | **str** | Description of the failure that occurred. | [optional] 
**error_details** | **List[Dict[str, str]]** | Information about the particular instance of the failure (supplied information depends on the type of failure). | [optional] 
## Example

```python
from lusid.models.error_detail import ErrorDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
type: Optional[StrictStr] = "example_type"
detail: Optional[StrictStr] = "example_detail"
error_details: Optional[List[Dict[str, StrictStr]]] = # Replace with your value
error_detail_instance = ErrorDetail(id=id, type=type, detail=detail, error_details=error_details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

