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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

price_scale_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
minimum_order_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
minimum_order_increment: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
trading_conventions_instance = TradingConventions(price_scale_factor=price_scale_factor, minimum_order_size=minimum_order_size, minimum_order_increment=minimum_order_increment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

