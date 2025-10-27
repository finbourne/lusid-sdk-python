# UpsertInstrumentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Instrument]**](Instrument.md) | The instruments which have been successfully updated or created. | [optional] 
**staged** | [**Dict[str, Instrument]**](Instrument.md) | The instruments that have been staged for updation or creation. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The instruments that could not be updated or created or were left unchanged without error along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Meta data associated with the upsert event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_instruments_response import UpsertInstrumentsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, Instrument]] = # Replace with your value
staged: Optional[Dict[str, Instrument]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, Optional[List[ResponseMetaData]]]] = # Replace with your value
links: Optional[List[Link]] = None
upsert_instruments_response_instance = UpsertInstrumentsResponse(href=href, values=values, staged=staged, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

