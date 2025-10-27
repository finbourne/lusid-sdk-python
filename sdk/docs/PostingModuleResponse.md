# PostingModuleResponse

A Posting Module definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**posting_module_code** | **str** | The code of the Posting Module. | 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Posting Module. | 
**description** | **str** | A description for the Posting Module. | [optional] 
**rules** | [**List[PostingModuleRule]**](PostingModuleRule.md) | The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection. | [optional] 
**status** | **str** | The Posting Module status. Can be Active, Inactive or Deleted. Defaults to Active. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.posting_module_response import PostingModuleResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
posting_module_code: StrictStr = "example_posting_module_code"
chart_of_accounts_id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
rules: Optional[List[PostingModuleRule]] = # Replace with your value
status: StrictStr = "example_status"
version: Optional[Version] = None
links: Optional[List[Link]] = None
posting_module_response_instance = PostingModuleResponse(href=href, posting_module_code=posting_module_code, chart_of_accounts_id=chart_of_accounts_id, display_name=display_name, description=description, rules=rules, status=status, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

