# RecResultItem

An individual item that makes up (one side of) a rec result. Polymorphic by rec type / item type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** | The polymorphic item-type discriminator (e.g. SettlementActivity, Holding, Transaction). Available values: SettlementActivity, Holding, Transaction. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**rule_and_attribute_values** | **Dict[str, Optional[str]]** | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. | [optional] [readonly] 
## Example

```python
from lusid.models.rec_result_item import RecResultItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

item_type: StrictStr = "example_item_type"
portfolio_id: ResourceId = # Replace with your value
rule_and_attribute_values: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
rec_result_item_instance = RecResultItem(item_type=item_type, portfolio_id=portfolio_id, rule_and_attribute_values=rule_and_attribute_values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

