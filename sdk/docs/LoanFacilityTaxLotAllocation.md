# LoanFacilityTaxLotAllocation

Contract-level state for a single tax lot on a single contract. These values live on the contract holding.                Each allocation names its own contract rather than being grouped under one, so the event carries a flat  list. A tax lot holding a balance on two contracts appears twice, once per contract.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_details** | [**ContractDetails**](ContractDetails.md) |  | 
**tax_lot_id** | **str** | The tax lot being set, identified by the transaction id of the trade that opened it. | 
**balance** | **float** | The desired settled balance for this tax lot on this contract, in the contract&#39;s own currency. This  replaces the pro-rata balance that the opening trade derived from the global facility state, which is  how a non-pro-rata position is expressed. | 
**balance_in_facility_ccy** | **float** | The desired balance expressed in the facility currency. Required when the contract currency differs  from the facility currency, and defaults to Balance otherwise. | [optional] 
**accrued_interest** | **float** | Interest accrued on this tax lot&#39;s balance on this contract, as at the start of the event&#39;s date, in  the contract&#39;s own currency. Distinct from the facility&#39;s own accrual on its undrawn amount - the two  are summed to give the accrued interest reported against the holding.                Omit it and the lot&#39;s accrual is left as it is, so a migrated lot accrues from its own trade date. | [optional] 
**pik_accrued_interest** | **float** | Payment-in-kind interest accrued on this tax lot, as at the start of the event&#39;s date, for a contract  carrying a PIK schedule. Tracked separately from cash-settled accrual and never derived. | [optional] 
## Example

```python
from lusid.models.loan_facility_tax_lot_allocation import LoanFacilityTaxLotAllocation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

contract_details: ContractDetails = # Replace with your value
tax_lot_id: StrictStr = "example_tax_lot_id"
balance: Union[StrictFloat, StrictInt] = # Replace with your value
balance_in_facility_ccy: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
accrued_interest: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
pik_accrued_interest: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
loan_facility_tax_lot_allocation_instance = LoanFacilityTaxLotAllocation(contract_details=contract_details, tax_lot_id=tax_lot_id, balance=balance, balance_in_facility_ccy=balance_in_facility_ccy, accrued_interest=accrued_interest, pik_accrued_interest=pik_accrued_interest)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

