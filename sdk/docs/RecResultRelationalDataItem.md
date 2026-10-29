# RecResultRelationalDataItem

A relational data point item within a rec result: one row of a relational dataset. The dataset and the unique  id of the data point identify the row. All rec types use this item shape. Also holds the display name of the  dataset.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relational_dataset_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**relational_dataset_definition_display_name** | **str** | The display name of the relational dataset definition the item&#39;s row belongs to, as it stood at the asAt the run read its data. Null where the run did not read it. | [optional] 
**relational_data_point_unique_id** | **str** | The unique id of the relational data point the run read, as minted by the relational dataset store. Opaque: compare it whole, do not parse it. | 
**item_type** | **str** | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction, SettlementActivity or RelationalDataPoint. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, both transaction rec types produce Transaction items, and a relational dataset side produces RelationalDataPoint items whatever the rec type. Available values: SettlementActivity, Holding, Transaction, ValuedHolding, RelationalDataPoint. | 
**rule_and_attribute_values** | **Dict[str, Optional[str]]** | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. | [optional] 
**writeback_suggestions** | [**List[WritebackSuggestion]**](WritebackSuggestion.md) | The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty. | [readonly] 
## Example

```python
from lusid.models.rec_result_relational_data_item import RecResultRelationalDataItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

relational_dataset_definition_id: ResourceId = # Replace with your value
relational_dataset_definition_display_name: Optional[StrictStr] = "example_relational_dataset_definition_display_name"
relational_data_point_unique_id: StrictStr = "example_relational_data_point_unique_id"
item_type: StrictStr = "example_item_type"
rule_and_attribute_values: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
writeback_suggestions: List[WritebackSuggestion] = # Replace with your value
rec_result_relational_data_item_instance = RecResultRelationalDataItem(relational_dataset_definition_id=relational_dataset_definition_id, relational_dataset_definition_display_name=relational_dataset_definition_display_name, relational_data_point_unique_id=relational_data_point_unique_id, item_type=item_type, rule_and_attribute_values=rule_and_attribute_values, writeback_suggestions=writeback_suggestions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

