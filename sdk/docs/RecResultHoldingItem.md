# RecResultHoldingItem

A holding-shaped item within a rec result: the holding a Holding or CashHolding rec reconciled  (itemType Holding), or the one a Valuation rec valued (itemType ValuedHolding). Also holds the display names  of the portfolio and the holding's instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_display_name** | **str** | The display name of the item&#39;s portfolio, as it stood at the asAt the run read its data. Null where the run did not read it. | [optional] 
**holding_id** | **str** | The holding identifier, at holding level: the same id whichever granularity the holding was read at, so that items of different rec types over one holding name it alike. | [optional] 
**tax_lot_id** | **str** | The tax lot the item is, where the source row was a single lot: a lot of a position read by tax lot, or a cash commitment. Null for an aggregated position and for a cash balance. Opaque: compare it whole, do not parse it. | [optional] 
**holding_instrument_scope** | **str** | The scope of the holding&#39;s instrument. Null where the source does not state one. | [optional] 
**holding_lusid_instrument_id** | **str** | The LUID of the holding&#39;s instrument. Null where the source does not state it. | [optional] 
**holding_instrument_name** | **str** | The name of the holding&#39;s instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it. | [optional] 
**item_type** | **str** | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction, SettlementActivity or RelationalDataPoint. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, both transaction rec types produce Transaction items, and a relational dataset side produces RelationalDataPoint items whatever the rec type. Available values: SettlementActivity, Holding, Transaction, ValuedHolding, RelationalDataPoint. | 
**rule_and_attribute_values** | **Dict[str, Optional[str]]** | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. | [optional] 
**writeback_suggestions** | [**List[WritebackSuggestion]**](WritebackSuggestion.md) | The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty. | [readonly] 
## Example

```python
from lusid.models.rec_result_holding_item import RecResultHoldingItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
portfolio_display_name: Optional[StrictStr] = "example_portfolio_display_name"
holding_id: Optional[StrictStr] = "example_holding_id"
tax_lot_id: Optional[StrictStr] = "example_tax_lot_id"
holding_instrument_scope: Optional[StrictStr] = "example_holding_instrument_scope"
holding_lusid_instrument_id: Optional[StrictStr] = "example_holding_lusid_instrument_id"
holding_instrument_name: Optional[StrictStr] = "example_holding_instrument_name"
item_type: StrictStr = "example_item_type"
rule_and_attribute_values: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
writeback_suggestions: List[WritebackSuggestion] = # Replace with your value
rec_result_holding_item_instance = RecResultHoldingItem(portfolio_id=portfolio_id, portfolio_display_name=portfolio_display_name, holding_id=holding_id, tax_lot_id=tax_lot_id, holding_instrument_scope=holding_instrument_scope, holding_lusid_instrument_id=holding_lusid_instrument_id, holding_instrument_name=holding_instrument_name, item_type=item_type, rule_and_attribute_values=rule_and_attribute_values, writeback_suggestions=writeback_suggestions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

