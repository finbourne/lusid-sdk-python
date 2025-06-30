# BatchUpsertInstrumentPropertiesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **Dict[str, List[ModelProperty]]** | The properties that have been successfully upserted | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The properties that could not be upserted along with a reason for their failure. | 
**as_at_date** | **datetime** | The as-at datetime at which properties were created or updated. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_upsert_instrument_properties_response import BatchUpsertInstrumentPropertiesResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
values: Dict[str, conlist(ModelProperty)] = # Replace with your value
failed: Dict[str, ErrorDetail] = # Replace with your value
as_at_date: datetime = # Replace with your value
links: Optional[conlist(Link)] = None
batch_upsert_instrument_properties_response_instance = BatchUpsertInstrumentPropertiesResponse(values=values, failed=failed, as_at_date=as_at_date, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

