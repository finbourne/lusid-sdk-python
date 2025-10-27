# UpdateGroupReconciliationComparisonRulesetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the ruleset | 
**reconciliation_type** | **str** | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; | 
**core_attribute_rules** | [**List[GroupReconciliationCoreAttributeRule]**](GroupReconciliationCoreAttributeRule.md) | The core comparison rules | 
**aggregate_attribute_rules** | [**List[GroupReconciliationAggregateAttributeRule]**](GroupReconciliationAggregateAttributeRule.md) | The aggregate comparison rules | 
## Example

```python
from lusid.models.update_group_reconciliation_comparison_ruleset_request import UpdateGroupReconciliationComparisonRulesetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
reconciliation_type: StrictStr = "example_reconciliation_type"
core_attribute_rules: List[GroupReconciliationCoreAttributeRule] = # Replace with your value
aggregate_attribute_rules: List[GroupReconciliationAggregateAttributeRule] = # Replace with your value
update_group_reconciliation_comparison_ruleset_request_instance = UpdateGroupReconciliationComparisonRulesetRequest(display_name=display_name, reconciliation_type=reconciliation_type, core_attribute_rules=core_attribute_rules, aggregate_attribute_rules=aggregate_attribute_rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

