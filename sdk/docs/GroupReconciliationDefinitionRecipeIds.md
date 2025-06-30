# GroupReconciliationDefinitionRecipeIds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**ResourceId**](ResourceId.md) |  | 
**right** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.group_reconciliation_definition_recipe_ids import GroupReconciliationDefinitionRecipeIds
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

left: ResourceId = # Replace with your value
right: ResourceId = # Replace with your value
group_reconciliation_definition_recipe_ids_instance = GroupReconciliationDefinitionRecipeIds(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

