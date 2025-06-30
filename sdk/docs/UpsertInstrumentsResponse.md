# UpsertInstrumentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Instrument]**](Instrument.md) | The instruments which have been successfully updated or created. | [optional] 
**staged** | [**Dict[str, Instrument]**](Instrument.md) | The instruments that have been staged for updation or creation. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The instruments that could not be updated or created or were left unchanged without error along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Meta data associated with the upsert event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_instruments_response import UpsertInstrumentsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, Instrument]] = # Replace with your value
staged: Optional[Dict[str, Instrument]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, conlist(ResponseMetaData)]] = # Replace with your value
links: Optional[conlist(Link)] = None
upsert_instruments_response_instance = UpsertInstrumentsResponse(href=href, values=values, staged=staged, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

