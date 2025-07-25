# CleardownModuleRulesUpdatedResponse

A Cleardown Module rules update response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[CleardownModuleRule]**](CleardownModuleRule.md) | The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.cleardown_module_rules_updated_response import CleardownModuleRulesUpdatedResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

rules: Optional[conlist(CleardownModuleRule)] = # Replace with your value
version: Optional[Version] = None
href: Optional[StrictStr] = "example_href"
links: Optional[conlist(Link)] = None
cleardown_module_rules_updated_response_instance = CleardownModuleRulesUpdatedResponse(rules=rules, version=version, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

