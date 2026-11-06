# UpsertComplianceRuleV3Request

A request to create or update a V3 compliance rule. A V3 rule's own record fully describes what it  checks: the subject it runs over, the filter selecting rows, the grouping and measure reducing them to a  number, and the check that number must satisfy. Shares no type with ComplianceV1/V2.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | 
**subject** | **str** | Available values: Holdings, Orders. | 
**filter** | [**ComplianceRuleV3FilterNode**](ComplianceRuleV3FilterNode.md) |  | [optional] 
**group_by** | **List[str]** |  | [optional] 
**measure** | [**ComplianceRuleV3Measure**](ComplianceRuleV3Measure.md) |  | 
**check** | [**ComplianceRuleV3Check**](ComplianceRuleV3Check.md) |  | 
**computed_filter** | [**ComplianceRuleV3ComputedFilter**](ComplianceRuleV3ComputedFilter.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_compliance_rule_v3_request import UpsertComplianceRuleV3Request
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
active: StrictBool
active:StrictBool = True
subject: StrictStr = "example_subject"
filter: Optional[ComplianceRuleV3FilterNode] = None
group_by: Optional[List[StrictStr]] = # Replace with your value
measure: ComplianceRuleV3Measure
check: ComplianceRuleV3Check
computed_filter: Optional[ComplianceRuleV3ComputedFilter] = # Replace with your value
upsert_compliance_rule_v3_request_instance = UpsertComplianceRuleV3Request(id=id, name=name, description=description, active=active, subject=subject, filter=filter, group_by=group_by, measure=measure, check=check, computed_filter=computed_filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

