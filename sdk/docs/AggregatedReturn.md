# AggregatedReturn

A list of Aggregated Returns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effectiveAt for the return. | 
**end_of_period** | **datetime** | The end of period date. For the monthly period this will be the Month End Date. | 
**opening_market_value** | **float** | The opening market value. | [optional] 
**closing_market_value** | **float** | The closing market value. | [optional] 
**metrics_value** | **Dict[str, float]** | The value for the specified metric. | 
**frequency** | **str** | Show the aggregated output returns on a Daily or Monthly period. | [optional] 
**composite_members** | **int** | The number of members in the Composite on the given day. | [optional] 
**composite_members_without_return** | [**List[ResourceId]**](ResourceId.md) | List containing Composite members which post no return on the given day. | [optional] 
**warnings** | **List[str]** | List of the warnings about the calculation of the aggregated return. | [optional] 

## Example

```python
from lusid.models.aggregated_return import AggregatedReturn

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedReturn from a JSON string
aggregated_return_instance = AggregatedReturn.from_json(json)
# print the JSON string representation of the object
print AggregatedReturn.to_json()

# convert the object into a dict
aggregated_return_dict = aggregated_return_instance.to_dict()
# create an instance of AggregatedReturn from a dict
aggregated_return_form_dict = aggregated_return.from_dict(aggregated_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


