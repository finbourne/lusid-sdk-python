# EstimateValuationDifference

How far apart the estimate-price and last-official-price valuations of the net dealing flow are.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The estimate-price net cashflow less the last-official-price net cashflow, in the fund currency. Negative when the last official price values the net flow higher. | 
**pct_of_nav** | **float** | The amount as a percentage of the fund&#39;s NAV at the previous valuation point. Absent when there is no previous NAV. | [optional] 
## Example

```python
from lusid.models.estimate_valuation_difference import EstimateValuationDifference
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amount: Union[StrictFloat, StrictInt] = # Replace with your value
pct_of_nav: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
estimate_valuation_difference_instance = EstimateValuationDifference(amount=amount, pct_of_nav=pct_of_nav)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

