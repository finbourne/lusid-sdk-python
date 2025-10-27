# StagingRuleApprovalCriteria

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_approvals** | **int** |  | [optional] 
**deciding_user** | **str** |  | [optional] 
**staging_user_can_decide** | **bool** |  | [optional] 
## Example

```python
from lusid.models.staging_rule_approval_criteria import StagingRuleApprovalCriteria
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

required_approvals: Optional[StrictInt] = # Replace with your value
required_approvals: Optional[StrictInt] = None
deciding_user: Optional[StrictStr] = "example_deciding_user"
staging_user_can_decide: Optional[StrictBool] = # Replace with your value
staging_user_can_decide:Optional[StrictBool] = None
staging_rule_approval_criteria_instance = StagingRuleApprovalCriteria(required_approvals=required_approvals, deciding_user=deciding_user, staging_user_can_decide=staging_user_can_decide)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

