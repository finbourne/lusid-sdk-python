# RecResultSettlementActivityItem

A settlement-activity item within a rec result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**activity_id** | **str** | The settlement activity identifier. | [optional] 
**transaction_id** | **str** | The transaction identifier. | [optional] 
**settlement_instruction_id** | **str** | The settlement instruction identifier. | [optional] 
**holding_impacts** | [**List[RecResultHoldingImpact]**](RecResultHoldingImpact.md) | The holdings, and where the source states them the tax lots, the item impacted. A distinct set ordered by holdingId then taxLotId; may be empty. An input transaction has not run the movements engine and impacts nothing yet. | 
**item_type** | **str** | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction or SettlementActivity. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, and both transaction rec types produce Transaction items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding. | 
**rule_and_attribute_values** | **Dict[str, Optional[str]]** | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. | [optional] 
## Example

```python
from lusid.models.rec_result_settlement_activity_item import RecResultSettlementActivityItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
activity_id: Optional[StrictStr] = "example_activity_id"
transaction_id: Optional[StrictStr] = "example_transaction_id"
settlement_instruction_id: Optional[StrictStr] = "example_settlement_instruction_id"
holding_impacts: List[RecResultHoldingImpact] = # Replace with your value
item_type: StrictStr = "example_item_type"
rule_and_attribute_values: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
rec_result_settlement_activity_item_instance = RecResultSettlementActivityItem(portfolio_id=portfolio_id, activity_id=activity_id, transaction_id=transaction_id, settlement_instruction_id=settlement_instruction_id, holding_impacts=holding_impacts, item_type=item_type, rule_and_attribute_values=rule_and_attribute_values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

