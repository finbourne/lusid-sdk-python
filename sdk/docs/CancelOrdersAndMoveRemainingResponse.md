# CancelOrdersAndMoveRemainingResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, CancelOrderAndMoveRemainingResult]**](CancelOrderAndMoveRemainingResult.md) | The orders which have been successfully cancelled, and any remaining quantities moved. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The orders that could not be cancelled, along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Meta data associated with the cancellation event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.cancel_orders_and_move_remaining_response import CancelOrdersAndMoveRemainingResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, CancelOrderAndMoveRemainingResult]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, conlist(ResponseMetaData)]] = # Replace with your value
links: Optional[conlist(Link)] = None
cancel_orders_and_move_remaining_response_instance = CancelOrdersAndMoveRemainingResponse(href=href, values=values, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

