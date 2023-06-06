# Aggregation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_effective_at** | **datetime** |  | [optional] 
**aggregation_as_at** | **datetime** |  | [optional] 
**href** | **str** |  | [optional] 
**data** | [**List[IDataRecord]**](IDataRecord.md) |  | [optional] 
**aggregation_currency** | **str** |  | [optional] 
**data_schema** | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 
**aggregation_failures** | [**List[AggregationMeasureFailureDetail]**](AggregationMeasureFailureDetail.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.aggregation import Aggregation

# TODO update the JSON string below
json = "{}"
# create an instance of Aggregation from a JSON string
aggregation_instance = Aggregation.from_json(json)
# print the JSON string representation of the object
print Aggregation.to_json()

# convert the object into a dict
aggregation_dict = aggregation_instance.to_dict()
# create an instance of Aggregation from a dict
aggregation_form_dict = aggregation.from_dict(aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


