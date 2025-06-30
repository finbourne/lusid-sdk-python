# AppendMarketData

Base class for types containing required data to append to complex market data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_type** | **str** | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData | 
## Example

```python
from lusid.models.append_market_data import AppendMarketData
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

market_data_type: StrictStr = "example_market_data_type"
append_market_data_instance = AppendMarketData(market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

