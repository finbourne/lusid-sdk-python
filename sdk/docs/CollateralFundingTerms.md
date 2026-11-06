# CollateralFundingTerms

What margin posted under the agreement costs us: the annual rate it is funded at and the basis it accrues on.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | The annual rate posted margin is funded at, as a fraction, for example 0.053 for 5.3%. Between -1 and 1. | 
**day_count_basis** | **int** | The number of days in the year the funding rate accrues over. Either 360 or 365. | 
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
collateral_funding_terms_instance = CollateralFundingTerms(rate=rate, day_count_basis=day_count_basis)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

