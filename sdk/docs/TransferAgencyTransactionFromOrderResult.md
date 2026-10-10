# TransferAgencyTransactionFromOrderResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**security_transaction_id** | **str** |  | [optional] 
**amended_cash_transaction_id** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**units** | **float** |  | [optional] 
## Example

```python
from lusid.models.transfer_agency_transaction_from_order_result import TransferAgencyTransactionFromOrderResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_id: Optional[ResourceId] = # Replace with your value
security_transaction_id: Optional[StrictStr] = "example_security_transaction_id"
amended_cash_transaction_id: Optional[StrictStr] = "example_amended_cash_transaction_id"
price: Optional[Union[StrictFloat, StrictInt]] = None
units: Optional[Union[StrictFloat, StrictInt]] = None
transfer_agency_transaction_from_order_result_instance = TransferAgencyTransactionFromOrderResult(order_id=order_id, security_transaction_id=security_transaction_id, amended_cash_transaction_id=amended_cash_transaction_id, price=price, units=units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

