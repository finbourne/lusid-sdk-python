# TaxReturnLoanRelationshipRow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_id** | **str** | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. | [optional] 
**instrument_id** | **str** | The LUSID unique identifier of the instrument. | [optional] 
**instrument_name** | **str** | The name of the instrument. | [optional] 
**portfolio_code** | **str** | The code of the portfolio the holding sits in, or the pooled marker for a company. | [optional] 
**ledger_amount** | **float** | The loan relationship credit or debit recorded in the ledger. | [optional] 
**uplift_excluded** | **float** | The uplift excluded from the loan relationship figure. | [optional] 
**net_credit_debit** | **float** | The net loan relationship credit or debit, after the uplift is excluded. | [optional] 
## Example

```python
from lusid.models.tax_return_loan_relationship_row import TaxReturnLoanRelationshipRow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_id: Optional[StrictStr] = "example_holding_id"
instrument_id: Optional[StrictStr] = "example_instrument_id"
instrument_name: Optional[StrictStr] = "example_instrument_name"
portfolio_code: Optional[StrictStr] = "example_portfolio_code"
ledger_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
uplift_excluded: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_credit_debit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_return_loan_relationship_row_instance = TaxReturnLoanRelationshipRow(holding_id=holding_id, instrument_id=instrument_id, instrument_name=instrument_name, portfolio_code=portfolio_code, ledger_amount=ledger_amount, uplift_excluded=uplift_excluded, net_credit_debit=net_credit_debit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

