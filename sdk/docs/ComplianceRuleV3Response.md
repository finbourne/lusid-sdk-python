# ComplianceRuleV3Response

A V3 compliance rule as returned by the API: its identity and administrative fields, its full  definition, and its version.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**subject** | **str** | Available values: Holdings, Orders. | [optional] 
**filter** | [**ComplianceRuleV3FilterNode**](ComplianceRuleV3FilterNode.md) |  | [optional] 
**group_by** | **List[str]** |  | [optional] 
**measure** | [**ComplianceRuleV3Measure**](ComplianceRuleV3Measure.md) |  | [optional] 
**check** | [**ComplianceRuleV3Check**](ComplianceRuleV3Check.md) |  | [optional] 
**computed_filter** | [**ComplianceRuleV3ComputedFilter**](ComplianceRuleV3ComputedFilter.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_v3_response import ComplianceRuleV3Response
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[ResourceId] = None
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
active: Optional[StrictBool] = None
active:Optional[StrictBool] = None
subject: Optional[StrictStr] = "example_subject"
filter: Optional[ComplianceRuleV3FilterNode] = None
group_by: Optional[List[StrictStr]] = # Replace with your value
measure: Optional[ComplianceRuleV3Measure] = None
check: Optional[ComplianceRuleV3Check] = None
computed_filter: Optional[ComplianceRuleV3ComputedFilter] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
compliance_rule_v3_response_instance = ComplianceRuleV3Response(id=id, name=name, description=description, active=active, subject=subject, filter=filter, group_by=group_by, measure=measure, check=check, computed_filter=computed_filter, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

