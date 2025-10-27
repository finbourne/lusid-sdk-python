# CheckDefinitionRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_key** | **str** | The key of the Rule. | [optional] 
**display_name** | **str** | The name of the Rule. | [optional] 
**description** | **str** | A description for the Rule. | [optional] 
**rule_formula** | **str** | The formula for the rule. | [optional] 
**severity** | **int** | Severity of the rule if formaula is not satisfied. | [optional] 
## Example

```python
from lusid.models.check_definition_rule import CheckDefinitionRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_key: Optional[StrictStr] = "example_rule_key"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
rule_formula: Optional[StrictStr] = "example_rule_formula"
severity: Optional[StrictInt] = # Replace with your value
severity: Optional[StrictInt] = None
check_definition_rule_instance = CheckDefinitionRule(rule_key=rule_key, display_name=display_name, description=description, rule_formula=rule_formula, severity=severity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

