# AcceptEstimateValuationPointResponse

The Valuation Point Data Response for AcceptEstimate called on the Fund and specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**candidate_valuation_point** | [**ValuationPointDataResponse**](ValuationPointDataResponse.md) |  | 
**latest_valuation_point** | [**ValuationPointDataResponse**](ValuationPointDataResponse.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.accept_estimate_valuation_point_response import AcceptEstimateValuationPointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptEstimateValuationPointResponse from a JSON string
accept_estimate_valuation_point_response_instance = AcceptEstimateValuationPointResponse.from_json(json)
# print the JSON string representation of the object
print AcceptEstimateValuationPointResponse.to_json()

# convert the object into a dict
accept_estimate_valuation_point_response_dict = accept_estimate_valuation_point_response_instance.to_dict()
# create an instance of AcceptEstimateValuationPointResponse from a dict
accept_estimate_valuation_point_response_form_dict = accept_estimate_valuation_point_response.from_dict(accept_estimate_valuation_point_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


