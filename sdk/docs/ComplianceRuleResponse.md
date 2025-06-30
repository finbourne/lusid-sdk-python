# ComplianceRuleResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**template_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**variation** | **str** |  | [optional] 
**portfolio_group_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**parameters** | [**Dict[str, ComplianceParameter]**](ComplianceParameter.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_response import ComplianceRuleResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist

id: Optional[ResourceId] = None
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
active: Optional[StrictBool] = None
active:Optional[StrictBool] = None
template_id: Optional[ResourceId] = # Replace with your value
variation: Optional[StrictStr] = "example_variation"
portfolio_group_id: Optional[ResourceId] = # Replace with your value
parameters: Optional[Dict[str, ComplianceParameter]] = None
properties: Optional[Dict[str, PerpetualProperty]] = None
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
compliance_rule_response_instance = ComplianceRuleResponse(id=id, name=name, description=description, active=active, template_id=template_id, variation=variation, portfolio_group_id=portfolio_group_id, parameters=parameters, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

