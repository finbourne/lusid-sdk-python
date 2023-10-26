# MarketQuote

The market quote for an observable which will be used to calibrate the market data,  including the format of the quote.  e.g. a volatility quote for a specific strike and expiry  the par rate of a swap                This is a slimmed down version of a full Quote that can be stored in our QuoteStore to  remove lineage, price source etc. for ease of use when creating complex market data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_type** | **str** | The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor, InflationAssumption, DirtyPrice | 
**value** | **float** | Numeric value of the quote | 

## Example

```python
from lusid.models.market_quote import MarketQuote

# TODO update the JSON string below
json = "{}"
# create an instance of MarketQuote from a JSON string
market_quote_instance = MarketQuote.from_json(json)
# print the JSON string representation of the object
print MarketQuote.to_json()

# convert the object into a dict
market_quote_dict = market_quote_instance.to_dict()
# create an instance of MarketQuote from a dict
market_quote_form_dict = market_quote.from_dict(market_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


