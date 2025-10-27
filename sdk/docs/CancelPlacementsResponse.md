# CancelPlacementsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, CancelledPlacementResult]**](CancelledPlacementResult.md) | The placements which have been successfully cancelled. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The placements that could not be cancelled, along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Meta data associated with the cancellation event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.cancel_placements_response import CancelPlacementsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, CancelledPlacementResult]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, Optional[List[ResponseMetaData]]]] = # Replace with your value
links: Optional[List[Link]] = None
cancel_placements_response_instance = CancelPlacementsResponse(href=href, values=values, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

