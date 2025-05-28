# QuoteSeriesId

The time invariant unique identifier of the quote. Combined with the effective datetime of the quote this  uniquely identifies the quote. This can be thought of as a unique identifier for a time series of quotes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The platform or vendor that provided the quote. The available values are: Client, DataScope, Lusid, Edi, TraderMade, FactSet, SIX, Bloomberg, Rimes, ICE, LSEG | 
**price_source** | **str** | The source or originator of the quote, e.g. a bank or financial institution. | [optional] 
**instrument_id** | **str** | The value of the instrument identifier that uniquely identifies the instrument that the quote is for, e.g. &#39;BBG00JX0P539&#39;. | 
**instrument_id_type** | **str** | The type of instrument identifier used to uniquely identify the instrument that the quote is for, e.g. &#39;Figi&#39;. The available values are: LusidInstrumentId, Figi, RIC, QuotePermId, Isin, CurrencyPair, ClientInternal, Sedol, Cusip | 
**quote_type** | **str** | The type of the quote. This allows for quotes other than prices e.g. rates or spreads to be used. The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor, InflationAssumption, DirtyPrice, PrincipalWriteOff, InterestDeferred, InterestShortfall, ConstituentWeightFactor | 
**field** | **str** | The field of the quote e.g. bid, mid, ask etc. This should be consistent across a time series of quotes. The allowed values depend on the provider according to the following rules: Client : *Any value is accepted*; DataScope : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;; Lusid : *Any value is accepted*; Edi : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;last&#39;; TraderMade : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;high&#39;, &#39;low&#39;; FactSet : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;; SIX : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;last&#39;, &#39;referencePrice&#39;, &#39;highPrice&#39;, &#39;lowPrice&#39;, &#39;maxRedemptionPrice&#39;, &#39;maxSubscriptionPrice&#39;, &#39;openPrice&#39;, &#39;bestBidPrice&#39;, &#39;lastBidPrice&#39;, &#39;bestAskPrice&#39;, &#39;lastAskPrice&#39;, &#39;finalSettlementOptions&#39;, &#39;finalSettlementFutures&#39;, &#39;valuationPriceAmount&#39;; Bloomberg : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;last&#39;; Rimes : &#39;bid&#39;, &#39;mid&#39;, &#39;ask&#39;, &#39;open&#39;, &#39;close&#39;, &#39;last&#39;; ICE : &#39;ask&#39;, &#39;bid&#39;, &#39;close&#39;, &#39;high&#39;, &#39;low&#39;, &#39;open&#39;, &#39;primaryExchangeTradePrice&#39;, &#39;vwap&#39;, &#39;mid&#39;; LSEG : &#39;ASK&#39;, &#39;BID&#39;, &#39;MID_PRICE&#39; | 

## Example

```python
from lusid.models.quote_series_id import QuoteSeriesId

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteSeriesId from a JSON string
quote_series_id_instance = QuoteSeriesId.from_json(json)
# print the JSON string representation of the object
print QuoteSeriesId.to_json()

# convert the object into a dict
quote_series_id_dict = quote_series_id_instance.to_dict()
# create an instance of QuoteSeriesId from a dict
quote_series_id_form_dict = quote_series_id.from_dict(quote_series_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


