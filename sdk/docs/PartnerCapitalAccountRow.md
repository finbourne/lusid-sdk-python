# PartnerCapitalAccountRow

One row of the capital account statement with its quarter-, year- and inception-to-date amounts.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_type** | **str** | The row type: BeginningCapital, Contributions, Distributions, TransfersIn, TransfersOut, NetOperatingIncome, ManagementFeesGross, ManagementFeeOffsets, RealisedGainLoss, UnrealisedGainLoss, CarriedInterest, EndingCapital, EqualisationInterest (equalisation interest credited to the partner&#39;s capital with no cash, reported after ending capital, which counts it, and only when there is some) or CallCredit (a memo of the call credit equalisations kept for the partner against its future calls: the quarter-to-date and year-to-date columns are its movement in each and inception to date is the credit left at the period end. It is a liability of the fund to the partner, not capital, so ending capital does not count it. Reported last, and only while a credit is left or one moved in the year). | 
**qtd** | **float** | The quarter-to-date amount for the row. | 
**ytd** | **float** | The year-to-date amount for the row. | 
**itd** | **float** | The inception-to-date amount for the row. | 
**details** | [**List[PartnerCapitalAccountRowDetail]**](PartnerCapitalAccountRowDetail.md) | Labelled parts of the row&#39;s total, each already included in the row&#39;s columns. Tax withheld from a distribution on the partner&#39;s behalf is counted as distributed and shown here as its own entry against the distribution it was withheld on. Empty for a row with nothing to break out. | [optional] 
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
details: Optional[List[PartnerCapitalAccountRowDetail]] = # Replace with your value
partner_capital_account_row_instance = PartnerCapitalAccountRow(row_type=row_type, qtd=qtd, ytd=ytd, itd=itd, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

