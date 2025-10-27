# UpsertInstrumentPropertiesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_date** | **datetime** | The as-at datetime at which properties were created or updated. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_instrument_properties_response import UpsertInstrumentPropertiesResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at_date: datetime = # Replace with your value
links: Optional[List[Link]] = None
upsert_instrument_properties_response_instance = UpsertInstrumentPropertiesResponse(as_at_date=as_at_date, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

