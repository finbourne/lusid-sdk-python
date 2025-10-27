# UpsertFlowConventionsRequest

Flow conventions that is to be stored in the convention data store.  Only one of these must be present.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_flow_conventions_request import UpsertFlowConventionsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

flow_conventions: Optional[FlowConventions] = # Replace with your value
upsert_flow_conventions_request_instance = UpsertFlowConventionsRequest(flow_conventions=flow_conventions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

