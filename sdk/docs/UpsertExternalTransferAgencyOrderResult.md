# UpsertExternalTransferAgencyOrderResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**dealing_point** | **datetime** |  | [optional] 
**late** | **bool** |  | [optional] 
**upserted_orders** | [**List[ResourceId]**](ResourceId.md) |  | [optional] 
**deleted_orders** | [**List[ResourceId]**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_external_transfer_agency_order_result import UpsertExternalTransferAgencyOrderResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
dealing_point: Optional[datetime] = # Replace with your value
late: Optional[StrictBool] = None
late:Optional[StrictBool] = None
upserted_orders: Optional[List[ResourceId]] = # Replace with your value
deleted_orders: Optional[List[ResourceId]] = # Replace with your value
upsert_external_transfer_agency_order_result_instance = UpsertExternalTransferAgencyOrderResult(fund_id=fund_id, dealing_point=dealing_point, late=late, upserted_orders=upserted_orders, deleted_orders=deleted_orders)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

