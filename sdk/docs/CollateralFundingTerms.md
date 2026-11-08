# CollateralFundingTerms

What margin posted under the agreement costs us: the annual rate it is funded at, the basis it accrues on and the  lending fee assumed forgone on a security with no fee quote of its own when collateral is ranked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | The annual rate posted margin is funded at, as a fraction, for example 0.053 for 5.3%. Between -1 and 1. | 
**day_count_basis** | **int** | The number of days in the year the funding rate accrues over. Either 360 or 365. | 
**default_lending_fee** | **float** | The annual lending fee, as a fraction, assumed forgone on a security with no fee quote of its own when collateral is ranked. Between 0 and 1. A security with no fee at all cannot be ranked. Optional. | [optional] 
## Example

```python
from lusid.models.collateral_funding_terms import CollateralFundingTerms
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rate: Union[StrictFloat, StrictInt] = # Replace with your value
day_count_basis: StrictInt = # Replace with your value
day_count_basis: StrictInt = 42
default_lending_fee: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
collateral_funding_terms_instance = CollateralFundingTerms(rate=rate, day_count_basis=day_count_basis, default_lending_fee=default_lending_fee)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

