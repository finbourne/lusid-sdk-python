# TaxReturnMemoRow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the period, for example the four-digit year. | [optional] 
**amount** | **float** | The amount, in pounds. | [optional] 
## Example

```python
from lusid.models.tax_return_memo_row import TaxReturnMemoRow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

label: Optional[StrictStr] = "example_label"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_return_memo_row_instance = TaxReturnMemoRow(label=label, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

