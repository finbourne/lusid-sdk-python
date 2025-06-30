# TemplateField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**specificity** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**availability** | **str** |  | 
**usage** | **List[str]** |  | 
## Example

```python
from lusid.models.template_field import TemplateField
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

field_name: StrictStr = "example_field_name"
specificity: StrictStr = "example_specificity"
description: StrictStr = "example_description"
type: StrictStr = "example_type"
availability: StrictStr = "example_availability"
usage: conlist(StrictStr) = # Replace with your value
template_field_instance = TemplateField(field_name=field_name, specificity=specificity, description=description, type=type, availability=availability, usage=usage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

