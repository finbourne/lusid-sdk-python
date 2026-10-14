# PartnerCapitalAccountRow

One row of the capital account statement with its quarter-, year- and inception-to-date amounts.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_type** | **str** | The row type: BeginningCapital, Contributions, Distributions, TransfersIn, TransfersOut, NetOperatingIncome, ManagementFeesGross, ManagementFeeOffsets, RealisedGainLoss, UnrealisedGainLoss, CarriedInterest or EndingCapital. | 
**qtd** | **float** | The quarter-to-date amount for the row. | 
**ytd** | **float** | The year-to-date amount for the row. | 
**itd** | **float** | The inception-to-date amount for the row. | 
## Example

```python
from lusid.models.partner_capital_account_row import PartnerCapitalAccountRow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

row_type: StrictStr = "example_row_type"
qtd: Union[StrictFloat, StrictInt] = # Replace with your value
ytd: Union[StrictFloat, StrictInt] = # Replace with your value
itd: Union[StrictFloat, StrictInt] = # Replace with your value
partner_capital_account_row_instance = PartnerCapitalAccountRow(row_type=row_type, qtd=qtd, ytd=ytd, itd=itd)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

