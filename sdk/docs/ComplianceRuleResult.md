# ComplianceRuleResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The unique identifierof a compliance rule | 
**rule_name** | **str** | The User-given name of the rule | 
**rule_description** | **str** | The User-given description of the rule | 
**portfolio** | [**ResourceId**](ResourceId.md) |  | 
**passed** | **bool** | The result of an individual compliance run, true if passed | 
**result_value** | **float** | The calculation result that was used to confirm a pass/fail | 
**rule_information_match** | **str** | The value matched by the rule | 
**rule_information_key** | **str** | The property key matched by the rule | 
**rule_lower_limit** | **float** | The lower limit of the rule | 
**rule_upper_limit** | **float** | The upper limit of the rule | 
## Example

```python
from lusid.models.compliance_rule_result import ComplianceRuleResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: StrictStr = "example_rule_id"
rule_name: StrictStr = "example_rule_name"
rule_description: StrictStr = "example_rule_description"
portfolio: ResourceId
passed: StrictBool = # Replace with your value
passed:StrictBool = True
result_value: Union[StrictFloat, StrictInt] = # Replace with your value
rule_information_match: StrictStr = "example_rule_information_match"
rule_information_key: StrictStr = "example_rule_information_key"
rule_lower_limit: Union[StrictFloat, StrictInt] = # Replace with your value
rule_upper_limit: Union[StrictFloat, StrictInt] = # Replace with your value
compliance_rule_result_instance = ComplianceRuleResult(rule_id=rule_id, rule_name=rule_name, rule_description=rule_description, portfolio=portfolio, passed=passed, result_value=result_value, rule_information_match=rule_information_match, rule_information_key=rule_information_key, rule_lower_limit=rule_lower_limit, rule_upper_limit=rule_upper_limit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

