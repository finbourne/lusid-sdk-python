# TransferAgencyExcludedOrder

An order left out of the sizing an estimate was struck from, with the reason it was left out.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**reason** | **str** |  | [optional] 
## Example

```python
from lusid.models.transfer_agency_excluded_order import TransferAgencyExcludedOrder
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_id: Optional[ResourceId] = # Replace with your value
reason: Optional[StrictStr] = "example_reason"
transfer_agency_excluded_order_instance = TransferAgencyExcludedOrder(order_id=order_id, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

