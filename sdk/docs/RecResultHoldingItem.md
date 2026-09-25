# RecResultHoldingItem

A holding-shaped item within a rec result: the holding a Holding or CashHolding rec reconciled  (itemType Holding), or the one a Valuation rec valued (itemType ValuedHolding).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**holding_id** | **str** | The holding identifier, at holding level: the same id whichever granularity the holding was read at, so that items of different rec types over one holding name it alike. | [optional] 
**tax_lot_id** | **str** | The tax lot the item is, where the source row was a single lot: a lot of a position read by tax lot, or a cash commitment. Null for an aggregated position and for a cash balance. Opaque: compare it whole, do not parse it. | [optional] 
**item_type** | **str** | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction or SettlementActivity. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, and both transaction rec types produce Transaction items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding. | 
**rule_and_attribute_values** | **Dict[str, Optional[str]]** | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. | [optional] 
## Example

```python
from lusid.models.rec_result_holding_item import RecResultHoldingItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
holding_id: Optional[StrictStr] = "example_holding_id"
tax_lot_id: Optional[StrictStr] = "example_tax_lot_id"
item_type: StrictStr = "example_item_type"
rule_and_attribute_values: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
rec_result_holding_item_instance = RecResultHoldingItem(portfolio_id=portfolio_id, holding_id=holding_id, tax_lot_id=tax_lot_id, item_type=item_type, rule_and_attribute_values=rule_and_attribute_values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

