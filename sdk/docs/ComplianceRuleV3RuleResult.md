# ComplianceRuleV3RuleResult

The aggregate result of one rule across every group it was evaluated over: the rule's overall status  (its worst group outcome) and the per-group results partitioned by outcome.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**status** | **str** | Available values: Passed, Failed, Warning, MissingData. | [optional] 
**results** | [**List[ComplianceRuleV3GroupResult]**](ComplianceRuleV3GroupResult.md) |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_v3_rule_result import ComplianceRuleV3RuleResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: Optional[ResourceId] = # Replace with your value
status: Optional[StrictStr] = "example_status"
results: Optional[List[ComplianceRuleV3GroupResult]] = None
compliance_rule_v3_rule_result_instance = ComplianceRuleV3RuleResult(rule_id=rule_id, status=status, results=results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

