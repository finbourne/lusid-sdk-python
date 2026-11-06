# CollateralOptimisationTerms

When a cheaper arrangement for the agreement's trades is worth recommending.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**novation_cost** | **float** | The one-off cost of novating trades away from the counterparty, in the agreement&#39;s base currency. At least 0. | 
**min_saving_per_day** | **float** | A change saving no more than this a day is not recommended. At least 0. | 
**max_payback_days** | **int** | A change whose one-off cost takes longer than this many days to earn back is not recommended. At least 0. | 
**max_per_agreement** | **int** | The most recommendations kept for the agreement, best first. Zero means no cap. At least 0. | 
## Example

```python
from lusid.models.collateral_optimisation_terms import CollateralOptimisationTerms
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

novation_cost: Union[StrictFloat, StrictInt] = # Replace with your value
min_saving_per_day: Union[StrictFloat, StrictInt] = # Replace with your value
max_payback_days: StrictInt = # Replace with your value
max_payback_days: StrictInt = 42
max_per_agreement: StrictInt = # Replace with your value
max_per_agreement: StrictInt = 42
collateral_optimisation_terms_instance = CollateralOptimisationTerms(novation_cost=novation_cost, min_saving_per_day=min_saving_per_day, max_payback_days=max_payback_days, max_per_agreement=max_per_agreement)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

