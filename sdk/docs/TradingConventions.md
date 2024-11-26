# TradingConventions

Common Trading details for exchange traded instruments like Futures and Bonds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_scale_factor** | **float** | The factor used to scale prices for the instrument. Currently used by LUSID when calculating cost  and notional amounts on transactions. Note this factor does not yet impact Valuation, PV, exposure,  all of which use the scale factor attached to the price quotes in the QuoteStore.  Must be positive and defaults to 1 if not set. | [optional] 
**minimum_order_size** | **float** | The Minimum Order Size  Must be non-negative and defaults to 0 if not set. | [optional] 
**minimum_order_increment** | **float** | The Minimum Order Increment  Must be non-negative and defaults to 0 if not set. | [optional] 

## Example

```python
from lusid.models.trading_conventions import TradingConventions

# TODO update the JSON string below
json = "{}"
# create an instance of TradingConventions from a JSON string
trading_conventions_instance = TradingConventions.from_json(json)
# print the JSON string representation of the object
print TradingConventions.to_json()

# convert the object into a dict
trading_conventions_dict = trading_conventions_instance.to_dict()
# create an instance of TradingConventions from a dict
trading_conventions_form_dict = trading_conventions.from_dict(trading_conventions_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


