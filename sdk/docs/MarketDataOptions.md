# MarketDataOptions

Base class for representing market data options in LUSID.  Abstractly, these are any options that one should be able to specify for ComplexMarketData entities.  For example, CurveOptions allows one to decide how the data provided in a discountFactorCurve is interpolated.  This base class should not be directly instantiated;  each supported MarketDataOptionsType has a corresponding inherited class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_options_type** | **str** | The available values are: CurveOptions | 
## Example

```python
from lusid.models.market_data_options import MarketDataOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

market_data_options_type: StrictStr = "example_market_data_options_type"
market_data_options_instance = MarketDataOptions(market_data_options_type=market_data_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

