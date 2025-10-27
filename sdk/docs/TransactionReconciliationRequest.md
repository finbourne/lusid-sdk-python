# TransactionReconciliationRequest

Specifies the parameter to be use when performing a Transaction Reconciliation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**right_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**mapping_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**from_transaction_date** | **datetime** |  | 
**to_transaction_date** | **datetime** |  | 
**as_at** | **datetime** |  | [optional] 
**property_keys** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.transaction_reconciliation_request import TransactionReconciliationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left_portfolio_id: ResourceId = # Replace with your value
right_portfolio_id: ResourceId = # Replace with your value
mapping_id: Optional[ResourceId] = # Replace with your value
from_transaction_date: datetime = # Replace with your value
to_transaction_date: datetime = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
property_keys: Optional[List[StrictStr]] = # Replace with your value
transaction_reconciliation_request_instance = TransactionReconciliationRequest(left_portfolio_id=left_portfolio_id, right_portfolio_id=right_portfolio_id, mapping_id=mapping_id, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, property_keys=property_keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

