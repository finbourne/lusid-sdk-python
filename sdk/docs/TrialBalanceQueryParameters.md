# TrialBalanceQueryParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**end** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**date_mode** | **str** | The mode of calculation of the trial balance. The available values are: ActivityDate, AccountingDate. | [optional] 
**general_ledger_profile_code** | **str** | The optional code of a general ledger profile used to decorate trial balance with levels. | [optional] 
**property_keys** | **List[str]** | A list of property keys from the &#39;Account&#39; domain to decorate onto the trial balance. | [optional] 
**exclude_cleardown_module** | **bool** | By deafult this flag is set to false, if this is set to true, no cleardown module will be applied to the trial balance. | [optional] 
## Example

```python
from lusid.models.trial_balance_query_parameters import TrialBalanceQueryParameters
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator

start: Optional[DateOrDiaryEntry] = None
end: Optional[DateOrDiaryEntry] = None
date_mode: Optional[StrictStr] = "example_date_mode"
general_ledger_profile_code: Optional[StrictStr] = "example_general_ledger_profile_code"
property_keys: Optional[conlist(StrictStr)] = # Replace with your value
exclude_cleardown_module: Optional[StrictBool] = # Replace with your value
exclude_cleardown_module:Optional[StrictBool] = None
trial_balance_query_parameters_instance = TrialBalanceQueryParameters(start=start, end=end, date_mode=date_mode, general_ledger_profile_code=general_ledger_profile_code, property_keys=property_keys, exclude_cleardown_module=exclude_cleardown_module)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

