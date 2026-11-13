# RecResultCustomEntityItem

An item within a rec result for one custom entity: one entity on a side of a LusidEntity rec of a custom entity  type. The entity unique id identifies it. The item also holds the display name and the identifiers of the entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The custom entity type of the entity the run read. It starts with a tilde. | 
**entity_unique_id** | **str** | The unique id of the entity the run read. It identifies the entity across scopes. | 
**entity_display_name** | **str** | The display name of the entity, as it stood at the dates the run read its side. | [optional] 
**identifiers** | **Dict[str, Optional[str]]** | The unique identifiers of the entity, keyed by identifier property key. The values are as at the dates the run read the side of the item, so they can differ from the current values. | 
**item_type** | **str** | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction, SettlementActivity, RelationalDataPoint or the entity type of a LusidEntity rec. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, both transaction rec types produce Transaction items, and a relational dataset side produces RelationalDataPoint items whatever the rec type. A LusidEntity rec produces items of its entity type, for example Instrument items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding, RelationalDataPoint, Instrument, LegalEntity, Portfolio, CustomEntity. | 
**rule_and_attribute_values** | **Dict[str, Optional[str]]** | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. | [optional] 
**writeback_suggestions** | [**List[WritebackSuggestion]**](WritebackSuggestion.md) | The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty. | [readonly] 
## Example

```python
from lusid.models.rec_result_custom_entity_item import RecResultCustomEntityItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: StrictStr = "example_entity_type"
entity_unique_id: StrictStr = "example_entity_unique_id"
entity_display_name: Optional[StrictStr] = "example_entity_display_name"
identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
item_type: StrictStr = "example_item_type"
rule_and_attribute_values: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
writeback_suggestions: List[WritebackSuggestion] = # Replace with your value
rec_result_custom_entity_item_instance = RecResultCustomEntityItem(entity_type=entity_type, entity_unique_id=entity_unique_id, entity_display_name=entity_display_name, identifiers=identifiers, item_type=item_type, rule_and_attribute_values=rule_and_attribute_values, writeback_suggestions=writeback_suggestions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

