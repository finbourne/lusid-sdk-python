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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

complex_market_data: Optional[List[EconomicDependencyWithComplexMarketData]] = # Replace with your value
quotes: Optional[List[EconomicDependencyWithQuote]] = # Replace with your value
market_data_overrides_instance = MarketDataOverrides(complex_market_data=complex_market_data, quotes=quotes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

