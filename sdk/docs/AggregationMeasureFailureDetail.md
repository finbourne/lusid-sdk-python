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

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationMeasureFailureDetail from a JSON string
aggregation_measure_failure_detail_instance = AggregationMeasureFailureDetail.from_json(json)
# print the JSON string representation of the object
print AggregationMeasureFailureDetail.to_json()

# convert the object into a dict
aggregation_measure_failure_detail_dict = aggregation_measure_failure_detail_instance.to_dict()
# create an instance of AggregationMeasureFailureDetail from a dict
aggregation_measure_failure_detail_form_dict = aggregation_measure_failure_detail.from_dict(aggregation_measure_failure_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


