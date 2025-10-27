# CheckDefinitionRuleSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_set_key** | **str** | The Key of the Rule Set. | [optional] 
**display_name** | **str** | The name of the Rule Set. | [optional] 
**description** | **str** | A description for the Rule Set. | [optional] 
**rule_set_filter** | **str** | A filter for the Rule Set to filter entity instances the rule set applies to. | [optional] 
**rules** | [**List[CheckDefinitionRule]**](CheckDefinitionRule.md) | A collection of rules for the Rule Set. | [optional] 
## Example

```python
from lusid.models.check_definition_rule_set import CheckDefinitionRuleSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_set_key: Optional[StrictStr] = "example_rule_set_key"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
rule_set_filter: Optional[StrictStr] = "example_rule_set_filter"
rules: Optional[List[CheckDefinitionRule]] = # Replace with your value
check_definition_rule_set_instance = CheckDefinitionRuleSet(rule_set_key=rule_set_key, display_name=display_name, description=description, rule_set_filter=rule_set_filter, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

