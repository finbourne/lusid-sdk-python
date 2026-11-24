# FundGroupTrialBalance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**nav_type_code** | **str** | The code of the NAV type the row, or result, was produced for. | [optional] 
**diary_entry_code** | **str** | The code of the valuation point the row was produced for. | [optional] 
**valuation_point_status** | **str** | The status of the valuation point the row was produced for, such as Final or Estimate. | [optional] 
**effective_end** | **datetime** | The effective end date of the valuation point the row was produced for. | [optional] 
**trial_balance** | [**TrialBalance**](TrialBalance.md) |  | [optional] 
## Example

```python
from lusid.models.fund_group_trial_balance import FundGroupTrialBalance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
diary_entry_code: Optional[StrictStr] = "example_diary_entry_code"
valuation_point_status: Optional[StrictStr] = "example_valuation_point_status"
effective_end: Optional[datetime] = # Replace with your value
trial_balance: Optional[TrialBalance] = # Replace with your value
fund_group_trial_balance_instance = FundGroupTrialBalance(fund_id=fund_id, nav_type_code=nav_type_code, diary_entry_code=diary_entry_code, valuation_point_status=valuation_point_status, effective_end=effective_end, trial_balance=trial_balance)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

