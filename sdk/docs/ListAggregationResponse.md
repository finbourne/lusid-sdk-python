# ListAggregationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_effective_at** | **datetime** |  | [optional] 
**aggregation_as_at** | **datetime** |  | [optional] 
**href** | **str** |  | [optional] 
**data** | **List[Dict[str, object]]** |  | [optional] 
**aggregation_currency** | **str** |  | [optional] 
**data_schema** | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 
**aggregation_failures** | [**List[AggregationMeasureFailureDetail]**](AggregationMeasureFailureDetail.md) |  | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.list_aggregation_response import ListAggregationResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

aggregation_effective_at: Optional[datetime] = # Replace with your value
aggregation_as_at: Optional[datetime] = # Replace with your value
href: Optional[StrictStr] = "example_href"
data: Optional[List[Dict[str, Any]]] = None
aggregation_currency: Optional[StrictStr] = "example_aggregation_currency"
data_schema: Optional[ResultDataSchema] = # Replace with your value
aggregation_failures: Optional[List[AggregationMeasureFailureDetail]] = # Replace with your value
recipe_id: Optional[ResourceId] = # Replace with your value
links: Optional[List[Link]] = None
list_aggregation_response_instance = ListAggregationResponse(aggregation_effective_at=aggregation_effective_at, aggregation_as_at=aggregation_as_at, href=href, data=data, aggregation_currency=aggregation_currency, data_schema=data_schema, aggregation_failures=aggregation_failures, recipe_id=recipe_id, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

