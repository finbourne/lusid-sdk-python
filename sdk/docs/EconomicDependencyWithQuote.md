# EconomicDependencyWithQuote

Container class pairing economic dependencies and quote data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**economic_dependency** | [**EconomicDependency**](EconomicDependency.md) |  | 
**metric_value** | [**MetricValue**](MetricValue.md) |  | 
**scale_factor** | **float** | Scale factor for the quote - this can be null, in which case we default to 1. | [optional] 

## Example

```python
from lusid.models.economic_dependency_with_quote import EconomicDependencyWithQuote

# TODO update the JSON string below
json = "{}"
# create an instance of EconomicDependencyWithQuote from a JSON string
economic_dependency_with_quote_instance = EconomicDependencyWithQuote.from_json(json)
# print the JSON string representation of the object
print EconomicDependencyWithQuote.to_json()

# convert the object into a dict
economic_dependency_with_quote_dict = economic_dependency_with_quote_instance.to_dict()
# create an instance of EconomicDependencyWithQuote from a dict
economic_dependency_with_quote_form_dict = economic_dependency_with_quote.from_dict(economic_dependency_with_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


