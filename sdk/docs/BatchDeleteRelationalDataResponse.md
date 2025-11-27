# BatchDeleteRelationalDataResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **Dict[str, Optional[str]]** | A list of data points that were successfully upserted. | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | A list of data points that failed to be upserted, along with the associated error message. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
## Example

```python
from lusid.models.batch_delete_relational_data_response import BatchDeleteRelationalDataResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Dict[str, Optional[StrictStr]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
href: Optional[StrictStr] = "example_href"
batch_delete_relational_data_response_instance = BatchDeleteRelationalDataResponse(values=values, failed=failed, href=href)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

