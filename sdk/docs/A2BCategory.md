# A2BCategory

A2B Category - one of the five major categories in the A2BDataRecord
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_currency** | [**A2BBreakdown**](A2BBreakdown.md) |  | [optional] 
**portfolio_currency** | [**A2BBreakdown**](A2BBreakdown.md) |  | [optional] 
## Example

```python
from lusid.models.a2_b_category import A2BCategory
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_currency: Optional[A2BBreakdown] = # Replace with your value
portfolio_currency: Optional[A2BBreakdown] = # Replace with your value
a2_b_category_instance = A2BCategory(holding_currency=holding_currency, portfolio_currency=portfolio_currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

