# TaxReturnSpreadInstalment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_period_id** | **str** | The label of the period whose deemed disposal is being spread. | [optional] 
**period_id** | **str** | The label of the period the amount falls into. | [optional] 
**fraction** | **float** | The fraction of the source period&#39;s spread amount that falls into the period. | [optional] 
**amount** | **float** | The amount, in pounds. | [optional] 
## Example

```python
from lusid.models.tax_return_spread_instalment import TaxReturnSpreadInstalment
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source_period_id: Optional[StrictStr] = "example_source_period_id"
period_id: Optional[StrictStr] = "example_period_id"
fraction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_return_spread_instalment_instance = TaxReturnSpreadInstalment(source_period_id=source_period_id, period_id=period_id, fraction=fraction, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

