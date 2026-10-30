# RecResultItem

An individual item that makes up (one side of) a rec result. Polymorphic by itemType; each value has a  corresponding inherited class.
## Example

```python
from lusid.models.rec_result_item import RecResultItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with RecResultItem 

rec_result_external_identifiers_item_instance = lusid.models.rec_result_external_identifiers_item.RecResultExternalIdentifiersItem(
                        entity_scope = '', 
                        entity_unique_id = '', 
                        entity_display_name = '', 
                        identifiers = {
                            'key' : ''
                            }, 
                        item_type = '', 
                        rule_and_attribute_values = {
                            'key' : ''
                            }, 
                        writeback_suggestions = [
                            lusid.models.writeback_suggestion.WritebackSuggestion(
                                writeback_type = '', )
                            ], )

rec_result_item_instance = RecResultItem(rec_result_external_identifiers_item_instance)

```
See all compatible oneOf types with RecResultItem


 * [RecResultHoldingItem](./RecResultHoldingItem.md)

 * [RecResultRelationalDataItem](./RecResultRelationalDataItem.md)

 * [RecResultSettlementActivityItem](./RecResultSettlementActivityItem.md)

 * [RecResultTransactionItem](./RecResultTransactionItem.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

