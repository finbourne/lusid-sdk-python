# AccruedFeeLine

A management fee accrued to one partner that the run left to its accrual rather than pooling.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The partner the fee was accrued to, when the accrual names one. | [optional] 
**amount** | **float** | The fee accrued to the partner, as the journal debits it. | 
## Example

```python
from lusid.models.accrued_fee_line import AccruedFeeLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: Optional[StrictStr] = "example_investor_record_id"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
accrued_fee_line_instance = AccruedFeeLine(investor_record_id=investor_record_id, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

