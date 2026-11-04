# UpsertExternalDealingEstimatesRequest

One dealing point's dealing estimates for the fund named in the route, as a third-party transfer agent sends them.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dealing_point** | **datetime** |  | 
**source** | [**ExternalDealingEstimateSource**](ExternalDealingEstimateSource.md) |  | 
**complete** | **bool** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 
**lines** | [**Dict[str, ExternalDealingEstimateLine]**](ExternalDealingEstimateLine.md) |  | 
## Example

```python
from lusid.models.upsert_external_dealing_estimates_request import UpsertExternalDealingEstimatesRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

dealing_point: datetime = # Replace with your value
source: ExternalDealingEstimateSource
complete: Optional[StrictBool] = None
complete:Optional[StrictBool] = None
sent_at: Optional[datetime] = # Replace with your value
lines: Dict[str, ExternalDealingEstimateLine]
upsert_external_dealing_estimates_request_instance = UpsertExternalDealingEstimatesRequest(dealing_point=dealing_point, source=source, complete=complete, sent_at=sent_at, lines=lines)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

