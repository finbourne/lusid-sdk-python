# TransactionSettlementInstruction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_instruction_id** | **str** | The instruction identifier. Unique within the portfolio. | 
**instruction_type** | **str** | The type of instruction which can be Complete or CancelAutomatic. Complete means that the instruction is intended to completely settle a settlement bucket. CancelAutomatic means that it is intended to cancel Automatic settlement. | 
**actual_settlement_date** | **datetime** | The date that settlement takes place. | 
**units** | **float** | The number of units for the instruction. | 
**transaction_id** | **str** | The ID for the transaction being instructed. | 
**settlement_category** | **str** | A category representing the set of movement types that this instruction applies to. | 
**lusid_instrument_id** | **str** | The LusidInstrumentId of the instrument being settled. | 
**contractual_settlement_date** | **datetime** | The contractual settlement date. Used to match the instruction to the correct settlement bucket. | [optional] 
**sub_holding_key_overrides** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Allows one or more sub-holding keys to be overridden for any movement being settled by an instruction. Providing a key and value will set the sub-holding key to the specified value; Providing a key only will nullify the sub-holding key. Not referenced sub-holding keys will not be impacted.  | [optional] 
**custodian_account_override** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the settlement instruction to a unique instrument. | 
**status** | **str** | The status of the settlement instruction - &#39;Invalid&#39;, &#39;Rejected&#39; &#39;Applied&#39; or &#39;Orphan&#39;. | [optional] 
## Example

```python
from lusid.models.transaction_settlement_instruction import TransactionSettlementInstruction
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr
from datetime import datetime
settlement_instruction_id: StrictStr = "example_settlement_instruction_id"
instruction_type: StrictStr = "example_instruction_type"
actual_settlement_date: datetime = # Replace with your value
units: Union[StrictFloat, StrictInt] = # Replace with your value
transaction_id: StrictStr = "example_transaction_id"
settlement_category: StrictStr = "example_settlement_category"
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
contractual_settlement_date: Optional[datetime] = # Replace with your value
sub_holding_key_overrides: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
custodian_account_override: Optional[ResourceId] = # Replace with your value
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
status: Optional[StrictStr] = "example_status"
transaction_settlement_instruction_instance = TransactionSettlementInstruction(settlement_instruction_id=settlement_instruction_id, instruction_type=instruction_type, actual_settlement_date=actual_settlement_date, units=units, transaction_id=transaction_id, settlement_category=settlement_category, lusid_instrument_id=lusid_instrument_id, contractual_settlement_date=contractual_settlement_date, sub_holding_key_overrides=sub_holding_key_overrides, custodian_account_override=custodian_account_override, instrument_identifiers=instrument_identifiers, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

