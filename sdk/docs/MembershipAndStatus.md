# MembershipAndStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Describes whether the entity is still a valid member of the data model. | 
**scope** | **str** | The scope of the unique identifier associated with the Custom Data Model. | 
**code** | **str** | The code of the unique identifier associated with the Custom Data Model. | 
**display_name** | **str** | The name of the Custom Data Model. | 
## Example

```python
from lusid.models.membership_and_status import MembershipAndStatus
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

status: StrictStr = "example_status"
scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
membership_and_status_instance = MembershipAndStatus(status=status, scope=scope, code=code, display_name=display_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

