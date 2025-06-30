# ComplianceTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**description** | **str** | The description of the Compliance Template | 
**tags** | **List[str]** | Tags for a Compliance Template | [optional] 
**variations** | [**List[ComplianceTemplateVariation]**](ComplianceTemplateVariation.md) | Variation details of a Compliance Template | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.compliance_template import ComplianceTemplate
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

id: ResourceId = # Replace with your value
description: StrictStr = "example_description"
tags: Optional[conlist(StrictStr)] = # Replace with your value
variations: conlist(ComplianceTemplateVariation) = # Replace with your value
links: Optional[conlist(Link)] = None
compliance_template_instance = ComplianceTemplate(id=id, description=description, tags=tags, variations=variations, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

