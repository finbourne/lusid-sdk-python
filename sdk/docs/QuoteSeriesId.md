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
**entity_unique_id** | **str** | The entity unique ID of the quote series. Together with the InstrumentId, EffectiveAt and AsAt this can uniquely identify a single quote. This field is readonly and cannot be provided on upsert. | [optional] [readonly] 
## Example

```python
from lusid.models.quote_series_id import QuoteSeriesId
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

provider: StrictStr = "example_provider"
price_source: Optional[StrictStr] = "example_price_source"
instrument_id: StrictStr = "example_instrument_id"
instrument_id_type: StrictStr = "example_instrument_id_type"
quote_type: StrictStr = "example_quote_type"
field: StrictStr = "example_field"
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
quote_series_id_instance = QuoteSeriesId(provider=provider, price_source=price_source, instrument_id=instrument_id, instrument_id_type=instrument_id_type, quote_type=quote_type, field=field, entity_unique_id=entity_unique_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

