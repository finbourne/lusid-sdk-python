# GetQuotesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Quote]**](Quote.md) | The quotes which have been successfully retrieved. | [optional] 
**not_found** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The quotes that could not be found along with a reason why. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The quotes that could not be retrieved due to an error along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.get_quotes_response import GetQuotesResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, Quote]] = # Replace with your value
not_found: Optional[Dict[str, ErrorDetail]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
get_quotes_response_instance = GetQuotesResponse(href=href, values=values, not_found=not_found, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

