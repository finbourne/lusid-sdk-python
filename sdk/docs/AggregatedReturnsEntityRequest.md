# AggregatedReturnsEntityRequest

The request body for the aggregated-returns (TWR) endpoint: the entity to calculate returns for, the  Returns entity that configures the calculation, the effective window, the metrics to calculate and the  period grid granularity. Supports a single `Portfolio` entity, the period `Return` metric and  a `Daily` grid.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**AggregatedReturnsEntityId**](AggregatedReturnsEntityId.md) |  | 
**returns_id** | [**ResourceId**](ResourceId.md) |  | 
**metrics** | [**List[ReturnsMetric]**](ReturnsMetric.md) |  | 
**period** | **str** | Available values: Daily, Monthly. | [optional] 
**from_effective_at** | **str** |  | [optional] 
**to_effective_at** | **str** |  | [optional] 
**as_at** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
## Example

```python
from lusid.models.aggregated_returns_entity_request import AggregatedReturnsEntityRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity: AggregatedReturnsEntityId
returns_id: ResourceId = # Replace with your value
metrics: List[ReturnsMetric]
period: Optional[StrictStr] = "example_period"
from_effective_at: Optional[StrictStr] = "example_from_effective_at"
to_effective_at: Optional[StrictStr] = "example_to_effective_at"
as_at: Optional[datetime] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
aggregated_returns_entity_request_instance = AggregatedReturnsEntityRequest(entity=entity, returns_id=returns_id, metrics=metrics, period=period, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

