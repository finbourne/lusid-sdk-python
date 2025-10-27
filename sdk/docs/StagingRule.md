# StagingRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The ID of the staging rule. | 
**description** | **str** | A description for the staging rule. | [optional] 
**status** | **str** | Whether the rule is &#39;Active&#39; or &#39;Inactive&#39;. | 
**match_criteria** | [**StagingRuleMatchCriteria**](StagingRuleMatchCriteria.md) |  | 
**approval_criteria** | [**StagingRuleApprovalCriteria**](StagingRuleApprovalCriteria.md) |  | 
## Example

```python
from lusid.models.staging_rule import StagingRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: StrictStr = "example_rule_id"
description: Optional[StrictStr] = "example_description"
status: StrictStr = "example_status"
match_criteria: StagingRuleMatchCriteria = # Replace with your value
approval_criteria: StagingRuleApprovalCriteria = # Replace with your value
staging_rule_instance = StagingRule(rule_id=rule_id, description=description, status=status, match_criteria=match_criteria, approval_criteria=approval_criteria)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

