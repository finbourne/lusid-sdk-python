# QueryableKeysForMetricsRequest

Specification of the metrics whose queryable key definitions are being requested.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **List[str]** | The address keys of the metrics to describe, given exactly as they would be supplied as the key of  a valuation request&#39;s metrics, for example &#39;Valuation/PV&#39; or &#39;Holding/Properties[Holding/MyScope/Rating]&#39;. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**effective_at** | **datetime** | The effective time to describe the metrics at, for definitions and entitlements that vary  along the effective timeline. Optional; defaults to the current time. | [optional] 
**as_at** | **datetime** | The as-at time to describe the metrics at. Optional; defaults to the latest. | [optional] 
## Example

```python
from lusid.models.queryable_keys_for_metrics_request import QueryableKeysForMetricsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

metrics: List[StrictStr] = # Replace with your value
recipe_id: Optional[ResourceId] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
queryable_keys_for_metrics_request_instance = QueryableKeysForMetricsRequest(metrics=metrics, recipe_id=recipe_id, effective_at=effective_at, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

