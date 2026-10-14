# CashInterest

Interest accrued on posted cash.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** | The name of the rate index. | 
**spread_bps** | **int** | The spread over the index, in basis points. | 
## Example

```python
from lusid.models.cash_interest import CashInterest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

index: StrictStr = "example_index"
spread_bps: StrictInt = # Replace with your value
spread_bps: StrictInt = 42
cash_interest_instance = CashInterest(index=index, spread_bps=spread_bps)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

