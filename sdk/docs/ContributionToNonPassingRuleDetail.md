# ContributionToNonPassingRuleDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**rule_status** | **str** | The status of the non-passing rule. | [optional] 
**breach_task_ids** | **List[str]** | The task ids associated with the compliance breach for this order&#39;s groups (if failing). | [optional] 
**likely_responsible_for_status** | **bool** | Whether this order is deemed as a likely contributor to the non-passing rule for this group. | [optional] 
## Example

```python
from lusid.models.contribution_to_non_passing_rule_detail import ContributionToNonPassingRuleDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: Optional[ResourceId] = # Replace with your value
rule_status: Optional[StrictStr] = "example_rule_status"
breach_task_ids: Optional[List[StrictStr]] = # Replace with your value
likely_responsible_for_status: Optional[StrictBool] = # Replace with your value
likely_responsible_for_status:Optional[StrictBool] = None
contribution_to_non_passing_rule_detail_instance = ContributionToNonPassingRuleDetail(rule_id=rule_id, rule_status=rule_status, breach_task_ids=breach_task_ids, likely_responsible_for_status=likely_responsible_for_status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

