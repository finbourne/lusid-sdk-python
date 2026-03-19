# GroupReconciliationFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | The filters for the left-side portfolio or portfolio group related data. | [optional] 
**right** | **str** | The filters for the right-side portfolio or portfolio group related data. | [optional] 
## Example

```python
from lusid.models.group_reconciliation_filters import GroupReconciliationFilters
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: Optional[StrictStr] = "example_left"
right: Optional[StrictStr] = "example_right"
group_reconciliation_filters_instance = GroupReconciliationFilters(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

