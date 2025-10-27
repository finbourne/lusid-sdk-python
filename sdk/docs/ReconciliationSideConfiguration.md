# ReconciliationSideConfiguration

Specification for one side of a valuations/positions scheduled reconciliation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**effective_at** | **datetime** |  | [optional] 
**as_at** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
## Example

```python
from lusid.models.reconciliation_side_configuration import ReconciliationSideConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

recipe_id: Optional[ResourceId] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
reconciliation_side_configuration_instance = ReconciliationSideConfiguration(recipe_id=recipe_id, effective_at=effective_at, as_at=as_at, currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

