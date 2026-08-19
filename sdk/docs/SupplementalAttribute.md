# SupplementalAttribute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The reference name of the supplemental attribute. | 
**left_formula** | **str** | Derivation formula evaluated against the left side of the reconciliation. | 
**right_formula** | **str** | Derivation formula evaluated against the right side of the reconciliation. | 
## Example

```python
from lusid.models.supplemental_attribute import SupplementalAttribute
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

attribute_name: StrictStr = "example_attribute_name"
left_formula: StrictStr = "example_left_formula"
right_formula: StrictStr = "example_right_formula"
supplemental_attribute_instance = SupplementalAttribute(attribute_name=attribute_name, left_formula=left_formula, right_formula=right_formula)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

