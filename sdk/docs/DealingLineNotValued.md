# DealingLineNotValued

A dealing line read for a swing decision that could not be valued into its share class currency, and why.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The identifier of the dealing order that could not be valued, as scope/code. | 
**share_class** | **str** | The share class the order deals in, keyed as the valuation point&#39;s share classes are. | [optional] 
**currency** | **str** | The currency the order&#39;s amount is in. Absent when the line carries no amount. | [optional] 
**reason** | **str** | Why the line could not be valued into the share class currency. | 
## Example

```python
from lusid.models.dealing_line_not_valued import DealingLineNotValued
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_id: StrictStr = "example_order_id"
share_class: Optional[StrictStr] = "example_share_class"
currency: Optional[StrictStr] = "example_currency"
reason: StrictStr = "example_reason"
dealing_line_not_valued_instance = DealingLineNotValued(order_id=order_id, share_class=share_class, currency=currency, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

