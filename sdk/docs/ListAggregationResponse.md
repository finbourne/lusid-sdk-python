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
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.list_aggregation_response import ListAggregationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAggregationResponse from a JSON string
list_aggregation_response_instance = ListAggregationResponse.from_json(json)
# print the JSON string representation of the object
print ListAggregationResponse.to_json()

# convert the object into a dict
list_aggregation_response_dict = list_aggregation_response_instance.to_dict()
# create an instance of ListAggregationResponse from a dict
list_aggregation_response_form_dict = list_aggregation_response.from_dict(list_aggregation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


