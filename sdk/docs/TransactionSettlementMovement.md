# TransactionSettlementMovement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The movement name (optional) | [optional] 
**type** | **str** | Movement types determine the impact of the movement on the holdings. The available values are: Settlement, Traded, StockMovement, FutureCash,  Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, Carry, CarryAsPnl, VariationMargin, Capital, Fee, Deferred, CashDeferred. | [optional] 
**units** | **float** | The number of units for the movement. | [optional] 
**direction** | **int** |  A multiplier to apply to Transaction amounts; the values are -1 to indicate to reverse the signs and 1 to indicate to use the signed values from the Transaction directly. For a typical Transaction with unsigned values, 1 means increase, -1 means decrease | [optional] 
**settlement_mode** | **str** | The mode of settlement for the movement which can either be Internal or External. An Internal movement will settle automatically on the contractual settlement date using TransactionConfiguration. An External movement will be determined by portfolio configuration and settlement instruction. | [optional] 
## Example

```python
from lusid.models.transaction_settlement_movement import TransactionSettlementMovement
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

name: Optional[StrictStr] = "example_name"
type: Optional[StrictStr] = "example_type"
units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
direction: Optional[StrictInt] = # Replace with your value
direction: Optional[StrictInt] = None
settlement_mode: Optional[StrictStr] = "example_settlement_mode"
transaction_settlement_movement_instance = TransactionSettlementMovement(name=name, type=type, units=units, direction=direction, settlement_mode=settlement_mode)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

