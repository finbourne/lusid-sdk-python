# ServiceApiEndpoints

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** |  | 
**endpoints** | [**List[ApiEndpoint]**](ApiEndpoint.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.service_api_endpoints import ServiceApiEndpoints
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

application: StrictStr = "example_application"
endpoints: List[ApiEndpoint]
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
service_api_endpoints_instance = ServiceApiEndpoints(application=application, endpoints=endpoints, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

