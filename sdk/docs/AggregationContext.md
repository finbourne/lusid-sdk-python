# AggregationContext

Aggregation context node. Whilst the market and pricing nodes concern themselves with which models are used and where the market data comes from, the aggregation  context determines how data is aggregated together. This controls the behaviour of the grouping and sql-like engine at the back of the valuation. For instance,  it controls conversion of currencies and whether the sql-like engine behaves more like ANSI or MySql SQL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**AggregationOptions**](AggregationOptions.md) |  | [optional] 

## Example

```python
from lusid.models.aggregation_context import AggregationContext

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationContext from a JSON string
aggregation_context_instance = AggregationContext.from_json(json)
# print the JSON string representation of the object
print AggregationContext.to_json()

# convert the object into a dict
aggregation_context_dict = aggregation_context_instance.to_dict()
# create an instance of AggregationContext from a dict
aggregation_context_form_dict = aggregation_context.from_dict(aggregation_context_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


