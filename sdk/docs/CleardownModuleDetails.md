# CleardownModuleDetails

A Cleardown Module request definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Cleardown Module. | 
**description** | **str** | A description for the Cleardown Module. | [optional] 
**status** | **str** | The Cleardown Module status. Can be Active or Inactive. Defaults to Active. | 
## Example

```python
from lusid.models.cleardown_module_details import CleardownModuleDetails
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
status: StrictStr = "example_status"
cleardown_module_details_instance = CleardownModuleDetails(display_name=display_name, description=description, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

