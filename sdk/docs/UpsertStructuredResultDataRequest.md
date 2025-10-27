# UpsertStructuredResultDataRequest

The details of the structured unit result data item to upsert into Lusid.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**StructuredResultDataId**](StructuredResultDataId.md) |  | 
**data** | [**StructuredResultData**](StructuredResultData.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_structured_result_data_request import UpsertStructuredResultDataRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StructuredResultDataId
data: Optional[StructuredResultData] = None
upsert_structured_result_data_request_instance = UpsertStructuredResultDataRequest(id=id, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

