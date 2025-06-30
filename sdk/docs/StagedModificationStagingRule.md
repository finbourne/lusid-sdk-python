# StagedModificationStagingRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staging_rule_set_id** | **str** | System generated unique id for the staging rule set. | [optional] 
**rule_id** | **str** | The ID of the staging rule. | [optional] 
**required_approvals** | **int** | The number of approvals required. If left blank, one approval is needed. | [optional] 
**current_user_can_decide** | **bool** | True or False indicating whether the current user can make a decision on the staged modification. | [optional] 
## Example

```python
from lusid.models.staged_modification_staging_rule import StagedModificationStagingRule
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr

staging_rule_set_id: Optional[StrictStr] = "example_staging_rule_set_id"
rule_id: Optional[StrictStr] = "example_rule_id"
required_approvals: Optional[StrictInt] = # Replace with your value
required_approvals: Optional[StrictInt] = None
current_user_can_decide: Optional[StrictBool] = # Replace with your value
current_user_can_decide:Optional[StrictBool] = None
staged_modification_staging_rule_instance = StagedModificationStagingRule(staging_rule_set_id=staging_rule_set_id, rule_id=rule_id, required_approvals=required_approvals, current_user_can_decide=current_user_can_decide)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

