# GroupReconciliationCoreAttributeValues

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_core_attributes** | [**List[ComparisonAttributeValuePair]**](ComparisonAttributeValuePair.md) | Core attribute names and values for the left hand entity being reconciled. | 
**right_core_attributes** | [**List[ComparisonAttributeValuePair]**](ComparisonAttributeValuePair.md) | Core attribute names and values for the right hand entity being reconciled. | 
## Example

```python
from lusid.models.group_reconciliation_core_attribute_values import GroupReconciliationCoreAttributeValues
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

left_core_attributes: conlist(ComparisonAttributeValuePair) = # Replace with your value
right_core_attributes: conlist(ComparisonAttributeValuePair) = # Replace with your value
group_reconciliation_core_attribute_values_instance = GroupReconciliationCoreAttributeValues(left_core_attributes=left_core_attributes, right_core_attributes=right_core_attributes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

