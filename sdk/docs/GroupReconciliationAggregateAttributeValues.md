# GroupReconciliationAggregateAttributeValues

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_aggregate_attributes** | [**List[ComparisonAttributeValuePair]**](ComparisonAttributeValuePair.md) | Aggregate attribute names and values for the left hand entity being reconciled. | 
**right_aggregate_attributes** | [**List[ComparisonAttributeValuePair]**](ComparisonAttributeValuePair.md) | Aggregate attribute names and values for the right hand entity being reconciled. | 
## Example

```python
from lusid.models.group_reconciliation_aggregate_attribute_values import GroupReconciliationAggregateAttributeValues
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left_aggregate_attributes: List[ComparisonAttributeValuePair] = # Replace with your value
right_aggregate_attributes: List[ComparisonAttributeValuePair] = # Replace with your value
group_reconciliation_aggregate_attribute_values_instance = GroupReconciliationAggregateAttributeValues(left_aggregate_attributes=left_aggregate_attributes, right_aggregate_attributes=right_aggregate_attributes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

