# TransactionConfigurationMovementData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movement_types** | **str** | Movement types determine the impact of the movement on the holdings. The available values are: Settlement, Traded, StockMovement, FutureCash,  Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, Carry, CarryAsPnl, VariationMargin, Capital, Fee, Deferred, CashDeferred. The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, Carry, CarryAsPnl, VariationMargin, Capital, Fee, LimitAdjustment, BalanceAdjustment, Deferred, CashDeferred | 
**side** | **str** | The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the &#39;security&#39; side of the transaction, ie the Instrument and Units; Side2 means the &#39;cash&#39; side, ie the Total Consideration | 
**direction** | **int** |  A multiplier to apply to Transaction amounts; the values are -1 to indicate to reverse the signs and 1 to indicate to use the signed values from the Transaction directly. For a typical Transaction with unsigned values, 1 means increase, -1 means decrease | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The properties associated with the underlying Movement | [optional] 
**mappings** | [**List[TransactionPropertyMapping]**](TransactionPropertyMapping.md) | This allows you to map a transaction property to a property on the underlying holding | [optional] 
**name** | **str** | The movement name (optional) | [optional] 
**movement_options** | **List[str]** | Allows extra specifications for the movement. The options currently available are &#39;DirectAdjustment&#39;, &#39;IncludesTradedInterest&#39;, &#39;Virtual&#39; and &#39;Income&#39; (works only with the movement type &#39;StockMovement&#39;). A movement type of &#39;StockMovement&#39; with an option of &#39;DirectAdjusment&#39; will allow you to adjust the units of a holding without affecting its cost base. You will, therefore, be able to reflect the impact of a stock split by loading a Transaction. | [optional] 
## Example

```python
from lusid.models.transaction_configuration_movement_data import TransactionConfigurationMovementData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

movement_types: StrictStr = "example_movement_types"
side: StrictStr = "example_side"
direction: StrictInt = # Replace with your value
direction: StrictInt = 42
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
mappings: Optional[List[TransactionPropertyMapping]] = # Replace with your value
name: Optional[StrictStr] = "example_name"
movement_options: Optional[List[StrictStr]] = # Replace with your value
transaction_configuration_movement_data_instance = TransactionConfigurationMovementData(movement_types=movement_types, side=side, direction=direction, properties=properties, mappings=mappings, name=name, movement_options=movement_options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

