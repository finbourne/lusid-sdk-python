# PortfolioReturnBreakdown

A list of Composite Breakdowns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**rate_of_return** | **float** | The return number. | [optional] 
**opening_market_value** | **float** | The opening market value. | [optional] 
**closing_market_value** | **float** | The closing market value. | [optional] 
**weight** | **float** | The weight of the constituent into the composite. | [optional] 
**constituents_in_the_composite** | **int** | The number of members in the Composite on the given day. | [optional] 
**constituents_missing** | **int** | The number of the constituents which have a missing return on that day. | [optional] 
**currency** | **str** | The currency of the portfolio. | [optional] 
**open_fx_rate** | **float** | The opening fxRate which is used in calculation. | [optional] 
**close_fx_rate** | **float** | The closing fxRate which is used in calculation. | [optional] 
**local_rate_of_return** | **float** | The rate of return in the local currency. | [optional] 
**local_opening_market_value** | **float** | The opening market value in the local currency. | [optional] 
**local_closing_market_value** | **float** | The closing market value in the local currency. | [optional] 
## Example

```python
from lusid.models.portfolio_return_breakdown import PortfolioReturnBreakdown
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

portfolio_id: ResourceId = # Replace with your value
rate_of_return: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
opening_market_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
closing_market_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
weight: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
constituents_in_the_composite: Optional[StrictInt] = # Replace with your value
constituents_in_the_composite: Optional[StrictInt] = None
constituents_missing: Optional[StrictInt] = # Replace with your value
constituents_missing: Optional[StrictInt] = None
currency: Optional[StrictStr] = "example_currency"
open_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
close_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
local_rate_of_return: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
local_opening_market_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
local_closing_market_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
portfolio_return_breakdown_instance = PortfolioReturnBreakdown(portfolio_id=portfolio_id, rate_of_return=rate_of_return, opening_market_value=opening_market_value, closing_market_value=closing_market_value, weight=weight, constituents_in_the_composite=constituents_in_the_composite, constituents_missing=constituents_missing, currency=currency, open_fx_rate=open_fx_rate, close_fx_rate=close_fx_rate, local_rate_of_return=local_rate_of_return, local_opening_market_value=local_opening_market_value, local_closing_market_value=local_closing_market_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

