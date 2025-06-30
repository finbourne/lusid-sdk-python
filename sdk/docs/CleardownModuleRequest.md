# CleardownModuleRequest

A Cleardown Module request definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Cleardown Module. | 
**display_name** | **str** | The name of the Cleardown Module. | 
**description** | **str** | A description for the Cleardown Module. | [optional] 
**rules** | [**List[CleardownModuleRule]**](CleardownModuleRule.md) | The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection. | [optional] 
## Example

```python
from lusid.models.cleardown_module_request import CleardownModuleRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
rules: Optional[conlist(CleardownModuleRule)] = # Replace with your value
cleardown_module_request_instance = CleardownModuleRequest(code=code, display_name=display_name, description=description, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

