# EconomicDependencyWithComplexMarketData

Container class pairing economic dependency and complex market data (i.e. discounting curves, etc.)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**economic_dependency** | [**EconomicDependency**](EconomicDependency.md) |  | 
**complex_market_data** | [**ComplexMarketData**](ComplexMarketData.md) |  | 

## Example

```python
from lusid.models.economic_dependency_with_complex_market_data import EconomicDependencyWithComplexMarketData

# TODO update the JSON string below
json = "{}"
# create an instance of EconomicDependencyWithComplexMarketData from a JSON string
economic_dependency_with_complex_market_data_instance = EconomicDependencyWithComplexMarketData.from_json(json)
# print the JSON string representation of the object
print EconomicDependencyWithComplexMarketData.to_json()

# convert the object into a dict
economic_dependency_with_complex_market_data_dict = economic_dependency_with_complex_market_data_instance.to_dict()
# create an instance of EconomicDependencyWithComplexMarketData from a dict
economic_dependency_with_complex_market_data_form_dict = economic_dependency_with_complex_market_data.from_dict(economic_dependency_with_complex_market_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


