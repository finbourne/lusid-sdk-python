# LabelValueSet

The set of string labels in a multi-value property.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | 
## Example

```python
from lusid.models.label_value_set import LabelValueSet
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

values: conlist(StrictStr, min_items=1) = Field(...)
label_value_set_instance = LabelValueSet(values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

