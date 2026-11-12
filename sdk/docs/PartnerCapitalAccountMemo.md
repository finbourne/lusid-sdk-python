# PartnerCapitalAccountMemo

The memo block of a capital account statement: commitment balances from the register at the period end.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment** | **float** | The partner&#39;s total commitment. | 
**uncalled_commitment** | **float** | The commitment not yet called. | 
**recallable** | **float** | Distributions that the fund may recall. | 
**available_commitment** | **float** | The commitment available to call, being uncalled plus recallable. | 
**contributions_receivable** | **float** | Called contributions not yet received from the partner, counting capital that was returned as recallable and has since been recalled. Omitted while a register line of the partner that has had returned capital marked recallable has not been rebuilt with recalled capital as a balance, since the figure could then miss an unpaid recall; the declared distributions are then served gross. | [optional] 
**distributions_declared_not_paid** | **float** | Distributions declared to the partner but not yet paid. | 
## Example

```python
from lusid.models.partner_capital_account_memo import PartnerCapitalAccountMemo
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

commitment: Union[StrictFloat, StrictInt] = # Replace with your value
uncalled_commitment: Union[StrictFloat, StrictInt] = # Replace with your value
recallable: Union[StrictFloat, StrictInt] = # Replace with your value
available_commitment: Union[StrictFloat, StrictInt] = # Replace with your value
contributions_receivable: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
distributions_declared_not_paid: Union[StrictFloat, StrictInt] = # Replace with your value
partner_capital_account_memo_instance = PartnerCapitalAccountMemo(commitment=commitment, uncalled_commitment=uncalled_commitment, recallable=recallable, available_commitment=available_commitment, contributions_receivable=contributions_receivable, distributions_declared_not_paid=distributions_declared_not_paid)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

