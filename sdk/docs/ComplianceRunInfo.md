# ComplianceRunInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | The unique identifier of a compliance run | 
**instigated_at** | **datetime** | The time the compliance run was launched (e.g. button pressed). Currently it is also both the as at and effective at time in whichthe rule set and portfolio data (including any pending trades if the run is pretrade) is taken for the caluation, although it may be possible to run compliance for historical effective at and as at dates in the future. | 
**completed_at** | **datetime** | The time the compliance run calculation was completed | 
**schedule** | **str** | Whether the compliance run was pre or post trade | 
**all_rules_passed** | **bool** | True if all rules passed, for all the portfolios they were assigned to | 
**has_results** | **bool** | False when no results have been returned eg. when no rules exist | 
**as_at** | **datetime** | Legacy AsAt time for backwards compatibility | 
## Example

```python
from lusid.models.compliance_run_info import ComplianceRunInfo
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
instigated_at: datetime = # Replace with your value
completed_at: datetime = # Replace with your value
schedule: StrictStr = "example_schedule"
all_rules_passed: StrictBool = # Replace with your value
all_rules_passed:StrictBool = True
has_results: StrictBool = # Replace with your value
has_results:StrictBool = True
as_at: datetime = # Replace with your value
compliance_run_info_instance = ComplianceRunInfo(run_id=run_id, instigated_at=instigated_at, completed_at=completed_at, schedule=schedule, all_rules_passed=all_rules_passed, has_results=has_results, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

