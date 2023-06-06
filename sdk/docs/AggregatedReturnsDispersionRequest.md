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

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedReturnsDispersionRequest from a JSON string
aggregated_returns_dispersion_request_instance = AggregatedReturnsDispersionRequest.from_json(json)
# print the JSON string representation of the object
print AggregatedReturnsDispersionRequest.to_json()

# convert the object into a dict
aggregated_returns_dispersion_request_dict = aggregated_returns_dispersion_request_instance.to_dict()
# create an instance of AggregatedReturnsDispersionRequest from a dict
aggregated_returns_dispersion_request_form_dict = aggregated_returns_dispersion_request.from_dict(aggregated_returns_dispersion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


