# MarketDataOverrides

Class which holds market data overrides to be used in valuation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complex_market_data** | [**List[EconomicDependencyWithComplexMarketData]**](EconomicDependencyWithComplexMarketData.md) | A list of EconomicDependency paired with quote data satisfying that economic dependency | [optional] 
**quotes** | [**List[EconomicDependencyWithQuote]**](EconomicDependencyWithQuote.md) | A list of EconomicDependency paired with a ComplexMarketData satisfying that economic dependency | [optional] 

## Example

```python
from lusid.models.market_data_overrides import MarketDataOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of MarketDataOverrides from a JSON string
market_data_overrides_instance = MarketDataOverrides.from_json(json)
# print the JSON string representation of the object
print MarketDataOverrides.to_json()

# convert the object into a dict
market_data_overrides_dict = market_data_overrides_instance.to_dict()
# create an instance of MarketDataOverrides from a dict
market_data_overrides_form_dict = market_data_overrides.from_dict(market_data_overrides_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


