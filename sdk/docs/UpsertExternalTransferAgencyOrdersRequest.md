# UpsertExternalTransferAgencyOrdersRequest

One dealing point's orders for one fund, as a third-party transfer agent sends them.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | 
**dealing_point** | **datetime** |  | 
**source** | [**ExternalTransferAgencyOrderSource**](ExternalTransferAgencyOrderSource.md) |  | 
**complete** | **bool** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 
**lines** | [**Dict[str, ExternalTransferAgencyOrderLine]**](ExternalTransferAgencyOrderLine.md) |  | 
## Example

```python
from lusid.models.upsert_external_transfer_agency_orders_request import UpsertExternalTransferAgencyOrdersRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: ResourceId = # Replace with your value
dealing_point: datetime = # Replace with your value
source: ExternalTransferAgencyOrderSource
complete: Optional[StrictBool] = None
complete:Optional[StrictBool] = None
sent_at: Optional[datetime] = # Replace with your value
lines: Dict[str, ExternalTransferAgencyOrderLine]
upsert_external_transfer_agency_orders_request_instance = UpsertExternalTransferAgencyOrdersRequest(fund_id=fund_id, dealing_point=dealing_point, source=source, complete=complete, sent_at=sent_at, lines=lines)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

