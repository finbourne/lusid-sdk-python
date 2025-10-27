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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
description: StrictStr = "example_description"
tags: Optional[List[StrictStr]] = # Replace with your value
variations: List[ComplianceTemplateVariation] = # Replace with your value
links: Optional[List[Link]] = None
compliance_template_instance = ComplianceTemplate(id=id, description=description, tags=tags, variations=variations, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

