# LabelValueSet

The set of string labels in a multi-value property.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | 
## Example

```python
from lusid.models.label_value_set import LabelValueSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[StrictStr]
label_value_set_instance = LabelValueSet(values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

