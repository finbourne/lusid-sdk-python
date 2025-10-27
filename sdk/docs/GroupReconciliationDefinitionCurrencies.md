# GroupReconciliationDefinitionCurrencies

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Currency for the left side of a reconciliation | 
**right** | **str** | Currency for the right side of a reconciliation | 
## Example

```python
from lusid.models.group_reconciliation_definition_currencies import GroupReconciliationDefinitionCurrencies
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: StrictStr = "example_left"
right: StrictStr = "example_right"
group_reconciliation_definition_currencies_instance = GroupReconciliationDefinitionCurrencies(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

