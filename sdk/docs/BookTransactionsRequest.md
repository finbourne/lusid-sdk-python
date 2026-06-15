# BookTransactionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_ids** | [**List[ResourceId]**](ResourceId.md) | A collection of Allocation IDs | 
**transaction_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | A collection of properties | [optional] 
**fx_instrument_type** | **str** | The type of FX instrument to create when settlement currency differs from portfolio base currency. Use None to suppress FX instrument and order creation. Defaults to None. Available values: None, FxForward, FxSpot. | [optional] 
## Example

```python
from lusid.models.book_transactions_request import BookTransactionsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

allocation_ids: List[ResourceId] = # Replace with your value
transaction_properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
fx_instrument_type: Optional[StrictStr] = "example_fx_instrument_type"
book_transactions_request_instance = BookTransactionsRequest(allocation_ids=allocation_ids, transaction_properties=transaction_properties, fx_instrument_type=fx_instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

