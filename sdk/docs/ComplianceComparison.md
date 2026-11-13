# ComplianceComparison

A single leaf comparison the check criterion made, re-evaluated for this group. A result of null is a comparison the  group held no data for (the criterion short-circuited past it).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predicate** | **str** |  | 
**left** | [**ComplianceComparisonOperand**](ComplianceComparisonOperand.md) |  | 
**operator** | **str** |  | 
**right** | [**ComplianceComparisonOperand**](ComplianceComparisonOperand.md) |  | 
**passed** | **bool** | Whether this leaf met its criterion for the group: true where it held, false for a breaching leaf. Absent for a  comparison the group carried no data for (the criterion short-circuited past it). | [optional] 
## Example

```python
from lusid.models.compliance_comparison import ComplianceComparison
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

predicate: StrictStr = "example_predicate"
left: ComplianceComparisonOperand
operator: StrictStr = "example_operator"
right: ComplianceComparisonOperand
passed: Optional[StrictBool] = # Replace with your value
passed:Optional[StrictBool] = None
compliance_comparison_instance = ComplianceComparison(predicate=predicate, left=left, operator=operator, right=right, passed=passed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

