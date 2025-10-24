# BatchUpsertRelationalDatasetsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, RelationalDataPointResponse]**](RelationalDataPointResponse.md) | A list of data points that were successfully upserted. | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | A list of data points that failed to be upserted, along with the associated error message. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_upsert_relational_datasets_response import BatchUpsertRelationalDatasetsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

values: Dict[str, RelationalDataPointResponse] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
href: Optional[StrictStr] = "example_href"
links: Optional[conlist(Link)] = None
batch_upsert_relational_datasets_response_instance = BatchUpsertRelationalDatasetsResponse(values=values, failed=failed, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

