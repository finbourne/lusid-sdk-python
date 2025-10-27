# ParticipationSetRequest

A request to create or update multiple Participations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[ParticipationRequest]**](ParticipationRequest.md) | A collection of ParticipationRequests. | [optional] 
## Example

```python
from lusid.models.participation_set_request import ParticipationSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

requests: Optional[List[ParticipationRequest]] = # Replace with your value
participation_set_request_instance = ParticipationSetRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

