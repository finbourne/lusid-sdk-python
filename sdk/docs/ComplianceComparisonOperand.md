# ComplianceComparisonOperand

One side of a comparison: the sub-expression that produced it and, where the group carried the data to evaluate it,  its value. The value is absent for a non-numeric constant, a reference list, or an operand the group held no data for.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** |  | 
**value** | **float** |  | [optional] 
## Example

```python
from lusid.models.compliance_comparison_operand import ComplianceComparisonOperand
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

expression: StrictStr = "example_expression"
value: Optional[Union[StrictFloat, StrictInt]] = None
compliance_comparison_operand_instance = ComplianceComparisonOperand(expression=expression, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

