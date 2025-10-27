# ShareClassAmount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_currency_amount** | **float** | The value of the amount in the fund currency. | [optional] 
**share_class_currency_amount** | **float** | The value of the amount in the share class currency. | [optional] 
## Example

```python
from lusid.models.share_class_amount import ShareClassAmount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_currency_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
share_class_currency_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
share_class_amount_instance = ShareClassAmount(fund_currency_amount=fund_currency_amount, share_class_currency_amount=share_class_currency_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

