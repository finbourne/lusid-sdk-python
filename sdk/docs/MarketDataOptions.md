# MarketDataOptions

Base class for representing market data options in LUSID.  Abstractly, these are any options that one should be able to specify for ComplexMarketData entities.  For example, CurveOptions allows one to decide how the data provided in a discountFactorCurve is interpolated.  This base class should not be directly instantiated;  each supported MarketDataOptionsType has a corresponding inherited class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_options_type** | **str** | The available values are: CurveOptions | 

## Example

```python
from lusid.models.market_data_options import MarketDataOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MarketDataOptions from a JSON string
market_data_options_instance = MarketDataOptions.from_json(json)
# print the JSON string representation of the object
print MarketDataOptions.to_json()

# convert the object into a dict
market_data_options_dict = market_data_options_instance.to_dict()
# create an instance of MarketDataOptions from a dict
market_data_options_form_dict = market_data_options.from_dict(market_data_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


