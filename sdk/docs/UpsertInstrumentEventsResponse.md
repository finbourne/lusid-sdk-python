# UpsertInstrumentEventsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, InstrumentEventHolder]**](InstrumentEventHolder.md) | The instrument events which have been successfully updated or inserted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The instrument events that could not be updated or inserted along with a reason for their failure. | [optional] 
**staged** | [**Dict[str, InstrumentEventHolder]**](InstrumentEventHolder.md) | The instrument events that have been staged pending approval. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_instrument_events_response import UpsertInstrumentEventsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, InstrumentEventHolder]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
staged: Optional[Dict[str, InstrumentEventHolder]] = # Replace with your value
links: Optional[List[Link]] = None
upsert_instrument_events_response_instance = UpsertInstrumentEventsResponse(href=href, values=values, failed=failed, staged=staged, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

