# TaxReturnExcludedRow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_id** | **str** | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. | [optional] 
**instrument_id** | **str** | The LUSID unique identifier of the instrument. | [optional] 
**instrument_name** | **str** | The name of the instrument. | [optional] 
**portfolio_code** | **str** | The code of the portfolio the holding sits in, or the pooled marker for a company. | [optional] 
**reason** | **str** | Why the holding is outside the return. | [optional] 
## Example

```python
from lusid.models.tax_return_excluded_row import TaxReturnExcludedRow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_id: Optional[StrictStr] = "example_holding_id"
instrument_id: Optional[StrictStr] = "example_instrument_id"
instrument_name: Optional[StrictStr] = "example_instrument_name"
portfolio_code: Optional[StrictStr] = "example_portfolio_code"
reason: Optional[StrictStr] = "example_reason"
tax_return_excluded_row_instance = TaxReturnExcludedRow(holding_id=holding_id, instrument_id=instrument_id, instrument_name=instrument_name, portfolio_code=portfolio_code, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

