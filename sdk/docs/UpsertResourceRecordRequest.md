# UpsertResourceRecordRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_scope** | **str** |  | 
**deployment_code** | **str** |  | 
**resource_id** | **str** |  | 
**format** | **str** |  | 
**resource_type** | **str** |  | 
**resource_state** | **object** |  | 
**dependencies** | **List[str]** |  | 
**tracking_state** | **object** |  | [optional] 
## Example

```python
from lusid.models.upsert_resource_record_request import UpsertResourceRecordRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

deployment_scope: StrictStr = "example_deployment_scope"
deployment_code: StrictStr = "example_deployment_code"
resource_id: StrictStr = "example_resource_id"
format: StrictStr = "example_format"
resource_type: StrictStr = "example_resource_type"
resource_state: Optional[Any] = # Replace with your value
dependencies: List[StrictStr]
tracking_state: Optional[Any] = # Replace with your value
upsert_resource_record_request_instance = UpsertResourceRecordRequest(deployment_scope=deployment_scope, deployment_code=deployment_code, resource_id=resource_id, format=format, resource_type=resource_type, resource_state=resource_state, dependencies=dependencies, tracking_state=tracking_state)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

