# TaxFundReconciliationProxyRow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_code** | **str** | The code of the member fund. | [optional] 
**amount** | **float** | The amount, in pounds. | [optional] 
## Example

```python
from lusid.models.tax_fund_reconciliation_proxy_row import TaxFundReconciliationProxyRow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_code: Optional[StrictStr] = "example_fund_code"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_fund_reconciliation_proxy_row_instance = TaxFundReconciliationProxyRow(fund_code=fund_code, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

