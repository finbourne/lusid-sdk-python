# MembershipAmendmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data_model_id** | [**ResourceId**](ResourceId.md) |  | 
**entity_type** | **str** | The type of the entity that is being added or removed from the Custom Data Model. | 
**entity_unique_id** | **str** | The entity unique identifier of the entity that is being added or removed from the Custom Data Model. | 
**operation** | **str** | The operation to be performed on the entity&#39;s membership in the Custom Data Model. Either &#39;Add&#39; or &#39;Remove&#39;. | 
## Example

```python
from lusid.models.membership_amendment_request import MembershipAmendmentRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

custom_data_model_id: ResourceId = # Replace with your value
entity_type: StrictStr = "example_entity_type"
entity_unique_id: StrictStr = "example_entity_unique_id"
operation: StrictStr = "example_operation"
membership_amendment_request_instance = MembershipAmendmentRequest(custom_data_model_id=custom_data_model_id, entity_type=entity_type, entity_unique_id=entity_unique_id, operation=operation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

