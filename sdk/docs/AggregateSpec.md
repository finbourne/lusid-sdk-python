# AggregateSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key that uniquely identifies a queryable address in Lusid. | 
**op** | **str** | The available values are: Sum, DefaultSum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears | 
**options** | **Dict[str, object]** | Additional options to apply when performing computations. Options that do not apply to the Key will be  ignored. Option values can be boolean, numeric, string or date-time. | [optional] 

## Example

```python
from lusid.models.aggregate_spec import AggregateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateSpec from a JSON string
aggregate_spec_instance = AggregateSpec.from_json(json)
# print the JSON string representation of the object
print AggregateSpec.to_json()

# convert the object into a dict
aggregate_spec_dict = aggregate_spec_instance.to_dict()
# create an instance of AggregateSpec from a dict
aggregate_spec_form_dict = aggregate_spec.from_dict(aggregate_spec_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


