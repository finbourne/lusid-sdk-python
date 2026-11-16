# TaxDeemedDisposalResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deterministic identifier of the deemed disposal, derived from the holding and date. | [optional] 
**holding_id** | **str** | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. | [optional] 
**instrument_id** | **str** | The LUSID unique identifier of the instrument. | [optional] 
**instrument_name** | **str** | The name of the instrument. | [optional] 
**portfolio_code** | **str** | The code of the portfolio the holding sits in, or the pooled marker for a company. | [optional] 
**var_date** | **datetime** | The date the deemed disposal arises, the end of the period. | [optional] 
**units** | **float** | The units disposed of. | [optional] 
**cost** | **float** | The allowable cost of the units disposed of. | [optional] 
**market_value** | **float** | The market value of the holding at the deemed-disposal date. | [optional] 
**net_amount** | **float** | The net deemed amount, gains less losses. | [optional] 
**notional** | **bool** | True when the deemed disposal is notional, as it is for a member fund, rather than an actual deemed disposal at company level. | [optional] 
## Example

```python
from lusid.models.tax_deemed_disposal_response import TaxDeemedDisposalResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
holding_id: Optional[StrictStr] = "example_holding_id"
instrument_id: Optional[StrictStr] = "example_instrument_id"
instrument_name: Optional[StrictStr] = "example_instrument_name"
portfolio_code: Optional[StrictStr] = "example_portfolio_code"
var_date: Optional[datetime] = # Replace with your value
units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cost: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
market_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
notional: Optional[StrictBool] = # Replace with your value
notional:Optional[StrictBool] = None
tax_deemed_disposal_response_instance = TaxDeemedDisposalResponse(id=id, holding_id=holding_id, instrument_id=instrument_id, instrument_name=instrument_name, portfolio_code=portfolio_code, var_date=var_date, units=units, cost=cost, market_value=market_value, net_amount=net_amount, notional=notional)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

