# ComplianceRuleV3CheckBound

A single bound of a check: a hard limit that must hold, plus an optional soft limit that raises a  warning without failing the rule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | [**ComplianceRuleV3DecimalBound**](ComplianceRuleV3DecimalBound.md) |  | 
**soft** | [**ComplianceRuleV3DecimalBound**](ComplianceRuleV3DecimalBound.md) |  | [optional] 
**hard_property** | **str** |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_v3_check_bound import ComplianceRuleV3CheckBound
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

hard: ComplianceRuleV3DecimalBound
soft: Optional[ComplianceRuleV3DecimalBound] = None
hard_property: Optional[StrictStr] = "example_hard_property"
compliance_rule_v3_check_bound_instance = ComplianceRuleV3CheckBound(hard=hard, soft=soft, hard_property=hard_property)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

