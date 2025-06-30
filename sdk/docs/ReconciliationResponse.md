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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

comparisons: Optional[conlist(ReconciliationLine)] = # Replace with your value
data_schema: Optional[ResultDataSchema] = # Replace with your value
reconciliation_response_instance = ReconciliationResponse(comparisons=comparisons, data_schema=data_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

