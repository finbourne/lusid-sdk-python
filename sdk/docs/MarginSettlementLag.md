# MarginSettlementLag

Business days between a margin call and settlement, by asset kind.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash** | **int** | The business days between a cash margin call and settlement. | 
**securities** | **int** | The business days between a securities margin call and settlement. | 
## Example

```python
from lusid.models.margin_settlement_lag import MarginSettlementLag
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cash: StrictInt = # Replace with your value
cash: StrictInt = 42
securities: StrictInt = # Replace with your value
securities: StrictInt = 42
margin_settlement_lag_instance = MarginSettlementLag(cash=cash, securities=securities)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

