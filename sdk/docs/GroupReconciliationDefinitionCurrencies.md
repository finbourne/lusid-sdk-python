# GroupReconciliationDefinitionCurrencies

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Currency for the left side of a reconciliation | 
**right** | **str** | Currency for the right side of a reconciliation | 
## Example

```python
from lusid.models.group_reconciliation_definition_currencies import GroupReconciliationDefinitionCurrencies
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

left: StrictStr = "example_left"
right: StrictStr = "example_right"
group_reconciliation_definition_currencies_instance = GroupReconciliationDefinitionCurrencies(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

