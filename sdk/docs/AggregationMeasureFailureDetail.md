# AggregationMeasureFailureDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**effective_at** | **datetime** |  | [optional] 
**measure** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
## Example

```python
from lusid.models.aggregation_measure_failure_detail import AggregationMeasureFailureDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
effective_at: Optional[datetime] = # Replace with your value
measure: Optional[StrictStr] = "example_measure"
reason: Optional[StrictStr] = "example_reason"
detail: Optional[StrictStr] = "example_detail"
aggregation_measure_failure_detail_instance = AggregationMeasureFailureDetail(id=id, effective_at=effective_at, measure=measure, reason=reason, detail=detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

