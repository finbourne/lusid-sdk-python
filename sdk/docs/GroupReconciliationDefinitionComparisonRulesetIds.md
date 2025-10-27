# GroupReconciliationDefinitionComparisonRulesetIds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_reconciliation** | [**ResourceId**](ResourceId.md) |  | [optional] 
**holding_reconciliation** | [**ResourceId**](ResourceId.md) |  | [optional] 
**valuation_reconciliation** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.group_reconciliation_definition_comparison_ruleset_ids import GroupReconciliationDefinitionComparisonRulesetIds
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_reconciliation: Optional[ResourceId] = # Replace with your value
holding_reconciliation: Optional[ResourceId] = # Replace with your value
valuation_reconciliation: Optional[ResourceId] = # Replace with your value
group_reconciliation_definition_comparison_ruleset_ids_instance = GroupReconciliationDefinitionComparisonRulesetIds(transaction_reconciliation=transaction_reconciliation, holding_reconciliation=holding_reconciliation, valuation_reconciliation=valuation_reconciliation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

