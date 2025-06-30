# UpsertPersonsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, Person]**](Person.md) | The Person(s) that have been successfully upserted | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The Person(s) that could not be upserted along with a reason for their failure. | 
**as_at_date** | **datetime** | The as-at datetime at which Person(s) were created or updated. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_persons_response import UpsertPersonsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
values: Dict[str, Person] = # Replace with your value
failed: Dict[str, ErrorDetail] = # Replace with your value
as_at_date: datetime = # Replace with your value
links: Optional[conlist(Link)] = None
upsert_persons_response_instance = UpsertPersonsResponse(values=values, failed=failed, as_at_date=as_at_date, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

