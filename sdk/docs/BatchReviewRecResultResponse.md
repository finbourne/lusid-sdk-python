# BatchReviewRecResultResponse

The response to a batch review request. Keyed by the client-supplied batch item key.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, BatchReviewRecResultItemResult]**](BatchReviewRecResultItemResult.md) | The successfully-processed batch items, keyed by the client-supplied batch item key. | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The failed batch items, keyed by the client-supplied batch item key. | [optional] 
**metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Response metadata, keyed by the client-supplied batch item key. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_review_rec_result_response import BatchReviewRecResultResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Dict[str, BatchReviewRecResultItemResult] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, Optional[List[ResponseMetaData]]]] = # Replace with your value
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
batch_review_rec_result_response_instance = BatchReviewRecResultResponse(values=values, failed=failed, metadata=metadata, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

