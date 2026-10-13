# FundPartnerBalances

The capital balances of one register line, in the commitment currency.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committed** | **float** | The committed capital. | 
**uncalled_commitment** | **float** | The commitment not yet called. | 
**paid_in** | **float** | The capital paid in. | 
**returned** | **float** | The capital returned. | 
**recallable** | **float** | The returned capital that may be recalled. | 
**unfunded** | **float** | The unfunded capital. | 
**funded** | **float** | The funded capital. | 
**outstanding_calls** | **float** | Capital called but not yet paid in. Omitted on a register line that has had returned capital marked recallable, since recalled capital is not yet tracked as a balance and the figure would exclude it. | [optional] 
## Example

```python
from lusid.models.fund_partner_balances import FundPartnerBalances
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

committed: Union[StrictFloat, StrictInt] = # Replace with your value
uncalled_commitment: Union[StrictFloat, StrictInt] = # Replace with your value
paid_in: Union[StrictFloat, StrictInt] = # Replace with your value
returned: Union[StrictFloat, StrictInt] = # Replace with your value
recallable: Union[StrictFloat, StrictInt] = # Replace with your value
unfunded: Union[StrictFloat, StrictInt] = # Replace with your value
funded: Union[StrictFloat, StrictInt] = # Replace with your value
outstanding_calls: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fund_partner_balances_instance = FundPartnerBalances(committed=committed, uncalled_commitment=uncalled_commitment, paid_in=paid_in, returned=returned, recallable=recallable, unfunded=unfunded, funded=funded, outstanding_calls=outstanding_calls)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

