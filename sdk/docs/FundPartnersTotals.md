# FundPartnersTotals

Totals across every register line of the fund, independent of paging.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committed** | **float** | The total committed capital across all partners. | 
**partner_count** | **int** | The number of partners (register lines) in the fund. | 
## Example

```python
from lusid.models.fund_partners_totals import FundPartnersTotals
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

committed: Union[StrictFloat, StrictInt] = # Replace with your value
partner_count: StrictInt = # Replace with your value
partner_count: StrictInt = 42
fund_partners_totals_instance = FundPartnersTotals(committed=committed, partner_count=partner_count)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

