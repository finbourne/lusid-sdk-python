# RulesInterval

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_range** | [**DateRange**](DateRange.md) |  | 
**rules** | [**List[AmortisationRule]**](AmortisationRule.md) | The rules of this rule set. | 
## Example

```python
from lusid.models.rules_interval import RulesInterval
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

effective_range: DateRange = # Replace with your value
rules: conlist(AmortisationRule, max_items=100) = Field(..., description="The rules of this rule set.")
rules_interval_instance = RulesInterval(effective_range=effective_range, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

