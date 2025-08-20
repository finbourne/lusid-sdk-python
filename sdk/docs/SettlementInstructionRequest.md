# SettlementInstructionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_instruction_id** | **str** |  | 
**transaction_id** | **str** |  | 
**settlement_category** | **str** |  | 
**instruction_type** | **str** |  | [optional] 
**instrument_identifiers** | **Dict[str, str]** |  | 
**contractual_settlement_date** | **datetime** |  | [optional] 
**actual_settlement_date** | **datetime** |  | 
**units** | **float** |  | 
**sub_holding_key_overrides** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**custodian_account_override** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.settlement_instruction_request import SettlementInstructionRequest
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr
from datetime import datetime
settlement_instruction_id: StrictStr = "example_settlement_instruction_id"
transaction_id: StrictStr = "example_transaction_id"
settlement_category: StrictStr = "example_settlement_category"
instruction_type: Optional[StrictStr] = "example_instruction_type"
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
contractual_settlement_date: Optional[datetime] = # Replace with your value
actual_settlement_date: datetime = # Replace with your value
units: Union[StrictFloat, StrictInt] = # Replace with your value
sub_holding_key_overrides: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
custodian_account_override: Optional[ResourceId] = # Replace with your value
settlement_instruction_request_instance = SettlementInstructionRequest(settlement_instruction_id=settlement_instruction_id, transaction_id=transaction_id, settlement_category=settlement_category, instruction_type=instruction_type, instrument_identifiers=instrument_identifiers, contractual_settlement_date=contractual_settlement_date, actual_settlement_date=actual_settlement_date, units=units, sub_holding_key_overrides=sub_holding_key_overrides, custodian_account_override=custodian_account_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

