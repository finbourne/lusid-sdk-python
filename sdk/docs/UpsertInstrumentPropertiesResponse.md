# UpsertInstrumentPropertiesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_date** | **datetime** | The as-at datetime at which properties were created or updated. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_instrument_properties_response import UpsertInstrumentPropertiesResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
as_at_date: datetime = # Replace with your value
links: Optional[conlist(Link)] = None
upsert_instrument_properties_response_instance = UpsertInstrumentPropertiesResponse(as_at_date=as_at_date, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

