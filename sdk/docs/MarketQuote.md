# MarketQuote

The market quote for an observable which will be used to calibrate the market data,  including the format of the quote.  e.g. a volatility quote for a specific strike and expiry  the par rate of a swap                This is a slimmed down version of a full Quote that can be stored in our QuoteStore to  remove lineage, price source etc. for ease of use when creating complex market data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_type** | **str** | The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor, InflationAssumption, DirtyPrice, PrincipalWriteOff, InterestDeferred, InterestShortfall, ConstituentWeightFactor | 
**value** | **float** | Numeric value of the quote | 
## Example

```python
from lusid.models.market_quote import MarketQuote
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

quote_type: StrictStr = "example_quote_type"
value: Union[StrictFloat, StrictInt] = # Replace with your value
market_quote_instance = MarketQuote(quote_type=quote_type, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

