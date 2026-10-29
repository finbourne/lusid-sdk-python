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

rec_result_holding_item_instance = lusid.models.rec_result_holding_item.RecResultHoldingItem(
                        portfolio_id = lusid.models.resource_id.ResourceId(
                            scope = '', 
                            code = '', ), 
                        portfolio_display_name = '', 
                        holding_id = '', 
                        tax_lot_id = '', 
                        holding_instrument_scope = '', 
                        holding_lusid_instrument_id = '', 
                        holding_instrument_name = '', 
                        item_type = '', 
                        rule_and_attribute_values = {
                            'key' : ''
                            }, 
                        writeback_suggestions = [
                            lusid.models.writeback_suggestion.WritebackSuggestion(
                                writeback_type = '', )
                            ], )

rec_result_item_instance = RecResultItem(rec_result_holding_item_instance)

```
See all compatible oneOf types with RecResultItem


 * [RecResultRelationalDataItem](./RecResultRelationalDataItem.md)

 * [RecResultSettlementActivityItem](./RecResultSettlementActivityItem.md)

 * [RecResultTransactionItem](./RecResultTransactionItem.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

