# QualifyingInvestmentsObservation

The qualifying-investments test result for one scheme on one day.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date the test was evaluated for. | 
**non_equity_percent** | **float** | The percentage of the scheme&#39;s assets that were qualifying (non-equity) investments on the date. | 
**is_bond_fund** | **bool** | Whether more than the threshold percentage of the scheme&#39;s assets were qualifying investments on the date, making it a bond fund. | 
## Example

```python
from lusid.models.qualifying_investments_observation import QualifyingInvestmentsObservation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: datetime = # Replace with your value
non_equity_percent: Union[StrictFloat, StrictInt] = # Replace with your value
is_bond_fund: StrictBool = # Replace with your value
is_bond_fund:StrictBool = True
qualifying_investments_observation_instance = QualifyingInvestmentsObservation(var_date=var_date, non_equity_percent=non_equity_percent, is_bond_fund=is_bond_fund)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

