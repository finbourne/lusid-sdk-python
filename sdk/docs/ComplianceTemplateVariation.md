# ComplianceTemplateVariation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label of a Compliance Template Variation | 
**description** | **str** | The description of the Compliance Template Variation | 
**required_parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | A parameter required by a Compliance Template Variation | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties associated with the Compliance Template Variation | 
**accepted_address_keys** | [**ResourceId**](ResourceId.md) |  | 
**steps** | [**List[ComplianceStep]**](ComplianceStep.md) | The steps expressed in this template, with their required parameters | 
**referenced_group_label** | **str** | The label of a given referenced group in a Compliance Rule Template Variation | [optional] 
## Example

```python
from lusid.models.compliance_template_variation import ComplianceTemplateVariation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

label: StrictStr = "example_label"
description: StrictStr = "example_description"
required_parameters: List[ComplianceTemplateParameter] = # Replace with your value
properties: Dict[str, PerpetualProperty] = # Replace with your value
accepted_address_keys: ResourceId = # Replace with your value
steps: List[ComplianceStep] = # Replace with your value
referenced_group_label: Optional[StrictStr] = "example_referenced_group_label"
compliance_template_variation_instance = ComplianceTemplateVariation(label=label, description=description, required_parameters=required_parameters, properties=properties, accepted_address_keys=accepted_address_keys, steps=steps, referenced_group_label=referenced_group_label)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

