# UpsertExternalDealingEstimateResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**dealing_point** | **datetime** |  | [optional] 
**late** | **bool** |  | [optional] 
**upserted_estimates** | [**List[ResourceId]**](ResourceId.md) |  | [optional] 
**deleted_estimates** | [**List[ResourceId]**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_external_dealing_estimate_result import UpsertExternalDealingEstimateResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
dealing_point: Optional[datetime] = # Replace with your value
late: Optional[StrictBool] = None
late:Optional[StrictBool] = None
upserted_estimates: Optional[List[ResourceId]] = # Replace with your value
deleted_estimates: Optional[List[ResourceId]] = # Replace with your value
upsert_external_dealing_estimate_result_instance = UpsertExternalDealingEstimateResult(fund_id=fund_id, dealing_point=dealing_point, late=late, upserted_estimates=upserted_estimates, deleted_estimates=deleted_estimates)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

