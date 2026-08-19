# CoreMatchingRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_name** | **str** | The reference name of the rule. | 
**left_formula** | **str** | Derivation formula evaluated against the left side of the reconciliation. | 
**right_formula** | **str** | Derivation formula evaluated against the right side of the reconciliation. | 
**is_case_sensitive** | **bool** | Whether the core rule comparison is case sensitive. Defaults to false. | [optional] 
## Example

```python
from lusid.models.core_matching_rule import CoreMatchingRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_name: StrictStr = "example_rule_name"
left_formula: StrictStr = "example_left_formula"
right_formula: StrictStr = "example_right_formula"
is_case_sensitive: Optional[StrictBool] = # Replace with your value
is_case_sensitive:Optional[StrictBool] = None
core_matching_rule_instance = CoreMatchingRule(rule_name=rule_name, left_formula=left_formula, right_formula=right_formula, is_case_sensitive=is_case_sensitive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

