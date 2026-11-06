# ComplianceRuleV3ComputedFilter

An optional inner test selecting survivors before the measure: an optional grouping, the measure to  compute per group, and the check the group's measure must satisfy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **List[str]** |  | [optional] 
**measure** | [**ComplianceRuleV3Measure**](ComplianceRuleV3Measure.md) |  | 
**check** | [**ComplianceRuleV3Check**](ComplianceRuleV3Check.md) |  | 
**select_outside_bounds** | **bool** |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_v3_computed_filter import ComplianceRuleV3ComputedFilter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

group_by: Optional[List[StrictStr]] = # Replace with your value
measure: ComplianceRuleV3Measure
check: ComplianceRuleV3Check
select_outside_bounds: Optional[StrictBool] = # Replace with your value
select_outside_bounds:Optional[StrictBool] = None
compliance_rule_v3_computed_filter_instance = ComplianceRuleV3ComputedFilter(group_by=group_by, measure=measure, check=check, select_outside_bounds=select_outside_bounds)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

