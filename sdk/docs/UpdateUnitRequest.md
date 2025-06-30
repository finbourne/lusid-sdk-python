# UpdateUnitRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from lusid.models.update_unit_request import UpdateUnitRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

code: Optional[StrictStr] = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
update_unit_request_instance = UpdateUnitRequest(code=code, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

