# TaxCostRecordRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_scope** | **str** | The scope of the portfolio the holding belongs to. | 
**portfolio_code** | **str** | The code of the portfolio the holding belongs to. | 
**instrument_identifier** | **str** | The LUSID instrument identifier (LUID) of the holding the tax cost applies to. | 
**nav_type_code** | **str** | The code of the NAV type the tax cost applies to. Optional; omit for the fund&#39;s primary NAV type. | [optional] 
**tax_cost** | **float** | The tax cost of the holding at the effective period end, in the fund&#39;s base currency. | 
**carried_forward_amount** | **float** | The amount carried forward into the next tax period, in the fund&#39;s base currency. | 
**effective_period_end** | **datetime** | The end date of the tax period the record applies to. | 
**source_valuation_point_id** | **str** | The identifier of the valuation point the record was derived from. Optional; omit for externally supplied records. | [optional] 
## Example

```python
from lusid.models.tax_cost_record_request import TaxCostRecordRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_scope: StrictStr = "example_portfolio_scope"
portfolio_code: StrictStr = "example_portfolio_code"
instrument_identifier: StrictStr = "example_instrument_identifier"
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
tax_cost: Union[StrictFloat, StrictInt] = # Replace with your value
carried_forward_amount: Union[StrictFloat, StrictInt] = # Replace with your value
effective_period_end: datetime = # Replace with your value
source_valuation_point_id: Optional[StrictStr] = "example_source_valuation_point_id"
tax_cost_record_request_instance = TaxCostRecordRequest(portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, instrument_identifier=instrument_identifier, nav_type_code=nav_type_code, tax_cost=tax_cost, carried_forward_amount=carried_forward_amount, effective_period_end=effective_period_end, source_valuation_point_id=source_valuation_point_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

