# SettlementActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | A unique identifier for the settlement activity row, composed from the portfolio, activity type and the underlying transaction or settlement instruction. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**activity_type** | **str** | The type of settlement activity: Expected for outstanding units that are due or overdue, or Settled for units that have settled. Available values: Expected, Settled. | 
**activity_basis** | **str** | The basis on which the settlement activity arose: Inferred for outstanding units, Automatic for units settled per the portfolio&#39;s settlement configuration, or Instruction for units settled by a settlement instruction. Available values: Inferred, Automatic, Instruction. | 
**activity_date** | **datetime** | The date of the settlement activity. For Expected activity this is the query&#39;s end activity date; for Automatic settlement it is the contractual settlement date; for Instruction settlement it is the instruction&#39;s actual settlement date. | 
**settlement_category** | **str** | The settlement category of the underlying movements. Available values: StockSettlement, CashSettlement, DeferredCashReceipt, NotApplicable. | 
**transaction_id** | **str** | The identifier of the transaction that gave rise to this settlement activity. Always populated for Expected and Settled activity. | [optional] 
**settlement_instruction_id** | **str** | The identifier of the settlement instruction that settled the activity. Populated only for Instruction settlement; null for Inferred and Automatic activity. | [optional] 
**holding_ids** | **List[int]** | The identifiers of the holdings whose movements contributed to this settlement activity. | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument identifier (LUID) of the instrument being settled. | 
**instrument_scope** | **str** | The scope in which the instrument is defined. | 
**contractual_settlement_date** | **datetime** | The contractual settlement date of the underlying movements. | 
**custodian_account_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**custodian_account_number** | **str** | The account number of the associated custodian account, if any. | [optional] 
**custodian_account_name** | **str** | The name of the associated custodian account, if any. | [optional] 
**units** | **float** | The signed number of units settled or expected to settle for this activity. | 
**direction** | **str** | The direction of the settlement from the portfolio&#39;s perspective. Available values: Debit, Credit. | 
**days_overdue** | **float** | The number of days the activity is overdue, calculated as the activity date minus the contractual settlement date. Zero for settled activity. | [optional] 
**transaction** | [**OutputTransaction**](OutputTransaction.md) |  | [optional] 
**settlement_instruction** | [**TransactionSettlementInstruction**](TransactionSettlementInstruction.md) |  | [optional] 
## Example

```python
from lusid.models.settlement_activity import SettlementActivity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

activity_id: StrictStr = "example_activity_id"
portfolio_id: ResourceId = # Replace with your value
activity_type: StrictStr = "example_activity_type"
activity_basis: StrictStr = "example_activity_basis"
activity_date: datetime = # Replace with your value
settlement_category: StrictStr = "example_settlement_category"
transaction_id: Optional[StrictStr] = "example_transaction_id"
settlement_instruction_id: Optional[StrictStr] = "example_settlement_instruction_id"
holding_ids: Optional[List[StrictInt]] = # Replace with your value
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
instrument_scope: StrictStr = "example_instrument_scope"
contractual_settlement_date: datetime = # Replace with your value
custodian_account_id: Optional[ResourceId] = # Replace with your value
custodian_account_number: Optional[StrictStr] = "example_custodian_account_number"
custodian_account_name: Optional[StrictStr] = "example_custodian_account_name"
units: Union[StrictFloat, StrictInt] = # Replace with your value
direction: StrictStr = "example_direction"
days_overdue: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transaction: Optional[OutputTransaction] = None
settlement_instruction: Optional[TransactionSettlementInstruction] = # Replace with your value
settlement_activity_instance = SettlementActivity(activity_id=activity_id, portfolio_id=portfolio_id, activity_type=activity_type, activity_basis=activity_basis, activity_date=activity_date, settlement_category=settlement_category, transaction_id=transaction_id, settlement_instruction_id=settlement_instruction_id, holding_ids=holding_ids, lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, contractual_settlement_date=contractual_settlement_date, custodian_account_id=custodian_account_id, custodian_account_number=custodian_account_number, custodian_account_name=custodian_account_name, units=units, direction=direction, days_overdue=days_overdue, transaction=transaction, settlement_instruction=settlement_instruction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

