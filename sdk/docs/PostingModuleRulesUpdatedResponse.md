# PostingModuleRulesUpdatedResponse

A Posting Module rules update response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[PostingModuleRule]**](PostingModuleRule.md) | The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.posting_module_rules_updated_response import PostingModuleRulesUpdatedResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rules: Optional[List[PostingModuleRule]] = # Replace with your value
version: Optional[Version] = None
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
posting_module_rules_updated_response_instance = PostingModuleRulesUpdatedResponse(rules=rules, version=version, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

