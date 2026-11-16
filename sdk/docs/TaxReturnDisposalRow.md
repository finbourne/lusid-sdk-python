# TaxReturnDisposalRow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_id** | **str** | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. | [optional] 
**instrument_id** | **str** | The LUSID unique identifier of the instrument. | [optional] 
**instrument_name** | **str** | The name of the instrument. | [optional] 
**portfolio_code** | **str** | The code of the portfolio the holding sits in, or the pooled marker for a company. | [optional] 
**disposal_date** | **datetime** | The date of the disposal. | [optional] 
**units** | **float** | The units disposed of. | [optional] 
**cost** | **float** | The allowable cost of the units disposed of. | [optional] 
**indexation_allowance_taken** | **float** | The indexation allowance deducted when arriving at the chargeable gain. | [optional] 
**chargeable_gain** | **float** | The chargeable gain or allowable loss on the disposal, negative for a loss. | [optional] 
## Example

```python
from lusid.models.tax_return_disposal_row import TaxReturnDisposalRow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_id: Optional[StrictStr] = "example_holding_id"
instrument_id: Optional[StrictStr] = "example_instrument_id"
instrument_name: Optional[StrictStr] = "example_instrument_name"
portfolio_code: Optional[StrictStr] = "example_portfolio_code"
disposal_date: Optional[datetime] = # Replace with your value
units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cost: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
indexation_allowance_taken: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
chargeable_gain: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_return_disposal_row_instance = TaxReturnDisposalRow(holding_id=holding_id, instrument_id=instrument_id, instrument_name=instrument_name, portfolio_code=portfolio_code, disposal_date=disposal_date, units=units, cost=cost, indexation_allowance_taken=indexation_allowance_taken, chargeable_gain=chargeable_gain)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

