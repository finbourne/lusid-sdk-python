# CleardownModuleResponse

A Cleardown Module definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**cleardown_module_code** | **str** | The code of the Cleardown Module. | 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Cleardown Module. | 
**description** | **str** | A description for the Cleardown Module. | [optional] 
**rules** | [**List[CleardownModuleRule]**](CleardownModuleRule.md) | The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection. | [optional] 
**status** | **str** | The Cleardown Module status. Can be Active, Inactive or Deleted. Defaults to Active. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.cleardown_module_response import CleardownModuleResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
cleardown_module_code: StrictStr = "example_cleardown_module_code"
chart_of_accounts_id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
rules: Optional[List[CleardownModuleRule]] = # Replace with your value
status: StrictStr = "example_status"
version: Optional[Version] = None
links: Optional[List[Link]] = None
cleardown_module_response_instance = CleardownModuleResponse(href=href, cleardown_module_code=cleardown_module_code, chart_of_accounts_id=chart_of_accounts_id, display_name=display_name, description=description, rules=rules, status=status, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

