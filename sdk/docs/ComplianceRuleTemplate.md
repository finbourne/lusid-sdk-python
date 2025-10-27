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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[ResourceId] = None
description: Optional[StrictStr] = "example_description"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
variations: Optional[List[ComplianceTemplateVariationDto]] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
compliance_rule_template_instance = ComplianceRuleTemplate(id=id, description=description, properties=properties, variations=variations, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

