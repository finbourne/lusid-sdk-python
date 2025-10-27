# ListAggregationReconciliation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**ListAggregationResponse**](ListAggregationResponse.md) |  | [optional] 
**right** | [**ListAggregationResponse**](ListAggregationResponse.md) |  | [optional] 
**diff** | **List[Dict[str, object]]** |  | [optional] 
**data_schema** | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 
## Example

```python
from lusid.models.list_aggregation_reconciliation import ListAggregationReconciliation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: Optional[ListAggregationResponse] = None
right: Optional[ListAggregationResponse] = None
diff: Optional[List[Dict[str, Any]]] = None
data_schema: Optional[ResultDataSchema] = # Replace with your value
list_aggregation_reconciliation_instance = ListAggregationReconciliation(left=left, right=right, diff=diff, data_schema=data_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

