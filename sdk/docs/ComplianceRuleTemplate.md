# ComplianceRuleTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**description** | **str** | The description of the Compliance Template | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties associated with the Compliance Template Variation | [optional] 
**variations** | [**List[ComplianceTemplateVariationDto]**](ComplianceTemplateVariationDto.md) | Variation details of a Compliance Template | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_template import ComplianceRuleTemplate
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

id: Optional[ResourceId] = None
description: Optional[StrictStr] = "example_description"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
variations: Optional[conlist(ComplianceTemplateVariationDto)] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
compliance_rule_template_instance = ComplianceRuleTemplate(id=id, description=description, properties=properties, variations=variations, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

