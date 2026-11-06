# ComplianceRunV3Response

The outcome of a V3 compliance run: the result of each rule that was run.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_results** | [**List[ComplianceRuleV3RuleResult]**](ComplianceRuleV3RuleResult.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.compliance_run_v3_response import ComplianceRunV3Response
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_results: Optional[List[ComplianceRuleV3RuleResult]] = # Replace with your value
links: Optional[List[Link]] = None
compliance_run_v3_response_instance = ComplianceRunV3Response(rule_results=rule_results, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

