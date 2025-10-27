# UpdatePlacementsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Placement]**](Placement.md) | The placements which have been successfully updated. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The placements that could not be updated, along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Meta data associated with the update event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.update_placements_response import UpdatePlacementsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, Placement]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, Optional[List[ResponseMetaData]]]] = # Replace with your value
links: Optional[List[Link]] = None
update_placements_response_instance = UpdatePlacementsResponse(href=href, values=values, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

