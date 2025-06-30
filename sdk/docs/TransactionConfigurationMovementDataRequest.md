# TransactionConfigurationMovementDataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movement_types** | **str** | . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, Carry, CarryAsPnl, VariationMargin, Capital, Fee, LimitAdjustment, BalanceAdjustment, Deferred, CashDeferred, UnsettledCashTypes | 
**side** | **str** | The movement side | 
**direction** | **int** | The movement direction | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The properties associated with the underlying Movement. | [optional] 
**mappings** | [**List[TransactionPropertyMappingRequest]**](TransactionPropertyMappingRequest.md) | This allows you to map a transaction property to a property on the underlying holding. | [optional] 
**name** | **str** | The movement name (optional) | [optional] 
**movement_options** | **List[str]** | Allows extra specifications for the movement. The options currently available are &#39;DirectAdjustment&#39;, &#39;IncludesTradedInterest&#39;, &#39;Virtual&#39; and &#39;Income&#39; (works only with the movement type &#39;StockMovement&#39;). A movement type of &#39;StockMovement&#39; with an option of &#39;DirectAdjusment&#39; will allow you to adjust the units of a holding without affecting its cost base. You will, therefore, be able to reflect the impact of a stock split by loading a Transaction. | [optional] 
## Example

```python
from lusid.models.transaction_configuration_movement_data_request import TransactionConfigurationMovementDataRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, constr, validator

movement_types: StrictStr = "example_movement_types"
side: StrictStr = "example_side"
direction: StrictInt = # Replace with your value
direction: StrictInt = 42
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
mappings: Optional[conlist(TransactionPropertyMappingRequest)] = # Replace with your value
name: Optional[StrictStr] = "example_name"
movement_options: Optional[conlist(StrictStr)] = # Replace with your value
transaction_configuration_movement_data_request_instance = TransactionConfigurationMovementDataRequest(movement_types=movement_types, side=side, direction=direction, properties=properties, mappings=mappings, name=name, movement_options=movement_options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

