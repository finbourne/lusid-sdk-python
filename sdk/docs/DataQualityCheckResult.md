# DataQualityCheckResult

Represents the result of a data quality check operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_definition_scope** | **str** | The scope of the check definition | [optional] 
**check_definition_code** | **str** | The code of the check definition | [optional] 
**check_definition_display_name** | **str** | The display name of the check definition | [optional] 
**check_run_as_at** | **datetime** | The timestamp when the check was run | [optional] 
**result_type** | **str** | The type of result from the check | [optional] 
**rule_set_key** | **str** | The key identifying the ruleset | [optional] 
**rule_set_display_name** | **str** | The display name of the ruleset | [optional] 
**rule_key** | **str** | The key identifying the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit) | [optional] 
**rule_display_name** | **str** | The display name of the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit) | [optional] 
**rule_description** | **str** | The description of the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit) | [optional] 
**rule_formula** | **str** | The formula of the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit) | [optional] 
**severity** | **int** | The severity level | [optional] 
**lusid_entity** | [**LusidEntityResult**](LusidEntityResult.md) |  | [optional] 
**count_rule_breaches** | **int** | The count of rule breaches (1 for RuleBreached, multiple for RuleBreachesOverLimit) | [optional] 
**error_detail** | **str** | Error details (for RulesetInvalid, RuleInvalid) | [optional] 
**result_id** | **str** | Unique identifier for the result in format: {{GUID of Check Definition}}-{{resultType}}-{{rulesetKey}}-{{ruleKey}}-{{entity GUID}} | [optional] 
## Example

```python
from lusid.models.data_quality_check_result import DataQualityCheckResult
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr
from datetime import datetime
check_definition_scope: Optional[StrictStr] = "example_check_definition_scope"
check_definition_code: Optional[StrictStr] = "example_check_definition_code"
check_definition_display_name: Optional[StrictStr] = "example_check_definition_display_name"
check_run_as_at: Optional[datetime] = # Replace with your value
result_type: Optional[StrictStr] = "example_result_type"
rule_set_key: Optional[StrictStr] = "example_rule_set_key"
rule_set_display_name: Optional[StrictStr] = "example_rule_set_display_name"
rule_key: Optional[StrictStr] = "example_rule_key"
rule_display_name: Optional[StrictStr] = "example_rule_display_name"
rule_description: Optional[StrictStr] = "example_rule_description"
rule_formula: Optional[StrictStr] = "example_rule_formula"
severity: Optional[StrictInt] = # Replace with your value
severity: Optional[StrictInt] = None
lusid_entity: Optional[LusidEntityResult] = # Replace with your value
count_rule_breaches: Optional[StrictInt] = # Replace with your value
count_rule_breaches: Optional[StrictInt] = None
error_detail: Optional[StrictStr] = "example_error_detail"
result_id: Optional[StrictStr] = "example_result_id"
data_quality_check_result_instance = DataQualityCheckResult(check_definition_scope=check_definition_scope, check_definition_code=check_definition_code, check_definition_display_name=check_definition_display_name, check_run_as_at=check_run_as_at, result_type=result_type, rule_set_key=rule_set_key, rule_set_display_name=rule_set_display_name, rule_key=rule_key, rule_display_name=rule_display_name, rule_description=rule_description, rule_formula=rule_formula, severity=severity, lusid_entity=lusid_entity, count_rule_breaches=count_rule_breaches, error_detail=error_detail, result_id=result_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

