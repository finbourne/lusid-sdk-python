# CompositeBreakdownResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**results** | **Dict[str, Optional[List[CompositeBreakdown]]]** | The Composite calculation with the constituens which were included. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.composite_breakdown_response import CompositeBreakdownResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
results: Dict[str, Optional[List[CompositeBreakdown]]] = # Replace with your value
links: Optional[List[Link]] = None
composite_breakdown_response_instance = CompositeBreakdownResponse(href=href, results=results, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

