# ReconciliationResponse

Class representing the set of comparisons that result from comparing holdings and their valuations between two separate evaluations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparisons** | [**List[ReconciliationLine]**](ReconciliationLine.md) | List of comparisons of left to right hand sides. | [optional] 
**data_schema** | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 
## Example

```python
from lusid.models.reconciliation_response import ReconciliationResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

comparisons: Optional[List[ReconciliationLine]] = # Replace with your value
data_schema: Optional[ResultDataSchema] = # Replace with your value
reconciliation_response_instance = ReconciliationResponse(comparisons=comparisons, data_schema=data_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

