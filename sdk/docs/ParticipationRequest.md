# ParticipationRequest

A request to create or update a Participation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placement_id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.participation_request import ParticipationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
placement_id: ResourceId = # Replace with your value
order_id: ResourceId = # Replace with your value
participation_request_instance = ParticipationRequest(id=id, placement_id=placement_id, order_id=order_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

