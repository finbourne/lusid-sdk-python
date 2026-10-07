# GlobalLoanFacilityContractState

The desired global state of a single FlexibleLoan contract. Balances are global - across all investors -  rather than investor specific.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_details** | [**ContractDetails**](ContractDetails.md) |  | 
**balance** | **float** | The desired global balance for this contract, in the contract&#39;s own currency. Must be non-negative. | 
**balance_in_facility_ccy** | **float** | The desired global balance expressed in the facility currency. Required when the contract currency  differs from the facility currency, and defaults to Balance otherwise. | [optional] 
**agency_fx_rate** | **float** | The agency FX rate converting contract currency to facility currency. Required when the contract  currency differs from the facility currency. When omitted it is derived from the two balances where  possible, and otherwise defaults to 1. | [optional] 
## Example

```python
from lusid.models.global_loan_facility_contract_state import GlobalLoanFacilityContractState
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

contract_details: ContractDetails = # Replace with your value
balance: Union[StrictFloat, StrictInt] = # Replace with your value
balance_in_facility_ccy: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
agency_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
global_loan_facility_contract_state_instance = GlobalLoanFacilityContractState(contract_details=contract_details, balance=balance, balance_in_facility_ccy=balance_in_facility_ccy, agency_fx_rate=agency_fx_rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

