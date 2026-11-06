# ComplianceRuleV3Check

The limits a measure's result is checked against: an optional upper bound, an optional lower bound, and  the unit both are expressed in.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Available values: Absolute, Percentage. | 
**upper** | [**ComplianceRuleV3CheckBound**](ComplianceRuleV3CheckBound.md) |  | [optional] 
**lower** | [**ComplianceRuleV3CheckBound**](ComplianceRuleV3CheckBound.md) |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_v3_check import ComplianceRuleV3Check
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

unit: StrictStr = "example_unit"
upper: Optional[ComplianceRuleV3CheckBound] = None
lower: Optional[ComplianceRuleV3CheckBound] = None
compliance_rule_v3_check_instance = ComplianceRuleV3Check(unit=unit, upper=upper, lower=lower)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

