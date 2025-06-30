# ParticipationSetRequest

A request to create or update multiple Participations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[ParticipationRequest]**](ParticipationRequest.md) | A collection of ParticipationRequests. | [optional] 
## Example

```python
from lusid.models.participation_set_request import ParticipationSetRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

requests: Optional[conlist(ParticipationRequest)] = # Replace with your value
participation_set_request_instance = ParticipationSetRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

