# AggregatedReturnsDispersionRequest

The request used in the AggregatedReturnsDispersionMetric.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_effective_at** | **str** | The end date for when the you want the dispersion to be calculated. | [optional] 
**years_count** | **int** | For how many years to calculate the dispersion. Default to 10. | [optional] 
**return_ids** | [**List[ResourceId]**](ResourceId.md) | The Scope and code of the returns. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**composite_method** | **str** | The method used to calculate the Portfolio performance: Equal/Asset. | [optional] 
**alternative_inception_date** | **str** | Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request. | [optional] 
## Example

```python
from lusid.models.aggregated_returns_dispersion_request import AggregatedReturnsDispersionRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, constr, validator

to_effective_at: Optional[StrictStr] = "example_to_effective_at"
years_count: Optional[StrictInt] = # Replace with your value
years_count: Optional[StrictInt] = None
return_ids: Optional[conlist(ResourceId)] = # Replace with your value
recipe_id: Optional[ResourceId] = # Replace with your value
composite_method: Optional[StrictStr] = "example_composite_method"
alternative_inception_date: Optional[StrictStr] = "example_alternative_inception_date"
aggregated_returns_dispersion_request_instance = AggregatedReturnsDispersionRequest(to_effective_at=to_effective_at, years_count=years_count, return_ids=return_ids, recipe_id=recipe_id, composite_method=composite_method, alternative_inception_date=alternative_inception_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

