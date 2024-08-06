# AggregatedReturnsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**results** | **Dict[str, List[AggregatedReturn]]** | Aggregated returns grouped by ReturnId | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.aggregated_returns_response import AggregatedReturnsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedReturnsResponse from a JSON string
aggregated_returns_response_instance = AggregatedReturnsResponse.from_json(json)
# print the JSON string representation of the object
print AggregatedReturnsResponse.to_json()

# convert the object into a dict
aggregated_returns_response_dict = aggregated_returns_response_instance.to_dict()
# create an instance of AggregatedReturnsResponse from a dict
aggregated_returns_response_form_dict = aggregated_returns_response.from_dict(aggregated_returns_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


