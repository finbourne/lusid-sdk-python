# UpsertExternalTransferAgencyOrdersResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | [**Dict[str, UpsertExternalTransferAgencyOrderResult]**](UpsertExternalTransferAgencyOrderResult.md) | A dictionary of successfully loaded sets, keyed by the request key. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | A dictionary of sets that could not be loaded, keyed by the request key, containing error details. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_external_transfer_agency_orders_response import UpsertExternalTransferAgencyOrdersResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

successes: Optional[Dict[str, UpsertExternalTransferAgencyOrderResult]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
upsert_external_transfer_agency_orders_response_instance = UpsertExternalTransferAgencyOrdersResponse(successes=successes, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

