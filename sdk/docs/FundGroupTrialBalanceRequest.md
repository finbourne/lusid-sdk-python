# FundGroupTrialBalanceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_type** | **str** | How the valuation point is chosen for each fund and NAV type. Available values: LatestApprovedNav (the latest Final valuation point on or before effectiveAt), LatestNav (the latest Final, Estimate or Candidate valuation point on or before effectiveAt), DateRange (every valuation point ending between start and end). AdHoc is not supported for the trial balance. Available values: LatestApprovedNav, LatestNav, AdHoc, DateRange. | 
**effective_at** | **str** | The date, or cut label, the valuation point is chosen for: the latest valuation point whose effective end is on or before this instant. Required for LatestApprovedNav and LatestNav; ignored for DateRange. | [optional] 
**start** | **str** | The first effective end date, or cut label, a DateRange run includes. Required for DateRange. | [optional] 
**end** | **str** | The last effective end date, or cut label, a DateRange run includes. Required for DateRange. | [optional] 
**nav_type_code** | **str** | When provided, every fund in the group is reported on this NAV type and a fund without it is reported as a failure. Otherwise each fund&#39;s NAV type comes from the reference list&#39;s NAV type codes hint, or its primary NAV type. | [optional] 
**statuses** | **List[str]** | Narrows the valuation point statuses a LatestNav or DateRange run considers. Defaults to all three. Available values: Final, Estimate, Candidate. | [optional] 
**output** | [**FundGroupReportOutput**](FundGroupReportOutput.md) |  | [optional] 
**general_ledger_profile_code** | **str** | The optional code of a General Ledger Profile used to decorate the rows with levels; it must exist in each fund&#39;s chart of accounts. | [optional] 
**exclude_cleardown_module** | **bool** | If this is set to true, no Cleardown Module will be applied to the Trial Balances. Defaults to false. | [optional] 
**variant** | **str** | The optional valuation point variant to report for each fund. | [optional] 
## Example

```python
from lusid.models.fund_group_trial_balance_request import FundGroupTrialBalanceRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_type: StrictStr = "example_run_type"
effective_at: Optional[StrictStr] = "example_effective_at"
start: Optional[StrictStr] = "example_start"
end: Optional[StrictStr] = "example_end"
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
statuses: Optional[List[StrictStr]] = # Replace with your value
output: Optional[FundGroupReportOutput] = None
general_ledger_profile_code: Optional[StrictStr] = "example_general_ledger_profile_code"
exclude_cleardown_module: Optional[StrictBool] = # Replace with your value
exclude_cleardown_module:Optional[StrictBool] = None
variant: Optional[StrictStr] = "example_variant"
fund_group_trial_balance_request_instance = FundGroupTrialBalanceRequest(run_type=run_type, effective_at=effective_at, start=start, end=end, nav_type_code=nav_type_code, statuses=statuses, output=output, general_ledger_profile_code=general_ledger_profile_code, exclude_cleardown_module=exclude_cleardown_module, variant=variant)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

