# FacilityReseedResult

The outcome of re-seeding a Facility's balance from the draws and repayments booked on it, or of a dry run of it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** | The code of the Facility re-seeded. | 
**currency** | **str** | The currency of the Facility, which every amount in the result is in. | 
**dry_run** | **bool** | Whether this was a dry run, which writes nothing. | 
**status** | **str** | The outcome. Available values: Reseeded (the balance was written from the booked draws and repayments), Unchanged (the balance already matched them, so nothing was written), WouldReseed (a dry run that would write the balance), Unattributable (a dry run that found draws or repayments naming the Facility on allocation maps whose structureMemberId is not their member fund; a re-seed is refused with 409 FacilityFlowsUnattributable until the maps are fixed). | 
**drawn_before** | **float** | What the stored balance had outstanding before the re-seed. Absent when the Facility had no balance. | [optional] 
**seed_version_before** | **int** | The seed rule the stored balance was seeded by before the re-seed; 0 for a balance stored before re-seeding existed, which the first draw or repayment on the Facility re-seeds. Absent when the Facility had no balance. | [optional] 
**drawn** | **float** | What the booked draws and repayments have outstanding, including events still in Booking status: the balance the Facility&#39;s limit is judged on. | 
**movement_count** | **int** | How many draws and repayments are booked on the Facility. | 
**booking_in_progress** | [**List[FacilityReseedFlow]**](FacilityReseedFlow.md) | The draws and repayments of events still in Booking status. They count in the balance and the headroom, are left out of both sides of the payable check as in flight, and are reported with a FacilityBookingInProgress warning. | 
**unattributable_flows** | [**List[FacilityReseedFlow]**](FacilityReseedFlow.md) | The draws and repayments naming the Facility on allocation maps whose structureMemberId is not their member fund: not a fund, or not the fund the map&#39;s fund structure places it on. Only listed by a dry run; empty otherwise. | 
**as_at** | **datetime** | The asAt the balance was written at, or the asAt a dry run or an unchanged re-seed read at. | 
**warnings** | [**List[Warning]**](Warning.md) | Warnings about the re-seed: FacilityBookingInProgress, or FacilityPayableBreak when the payable check finds breaks. | [optional] 
**payable_check** | [**FacilityPayableCheck**](FacilityPayableCheck.md) |  | 
## Example

```python
from lusid.models.facility_reseed_result import FacilityReseedResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

facility_code: StrictStr = "example_facility_code"
currency: StrictStr = "example_currency"
dry_run: StrictBool = # Replace with your value
dry_run:StrictBool = True
status: StrictStr = "example_status"
drawn_before: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
seed_version_before: Optional[StrictInt] = # Replace with your value
seed_version_before: Optional[StrictInt] = None
drawn: Union[StrictFloat, StrictInt] = # Replace with your value
movement_count: StrictInt = # Replace with your value
movement_count: StrictInt = 42
booking_in_progress: List[FacilityReseedFlow] = # Replace with your value
unattributable_flows: List[FacilityReseedFlow] = # Replace with your value
as_at: datetime = # Replace with your value
warnings: Optional[List[Warning]] = # Replace with your value
payable_check: FacilityPayableCheck = # Replace with your value
facility_reseed_result_instance = FacilityReseedResult(facility_code=facility_code, currency=currency, dry_run=dry_run, status=status, drawn_before=drawn_before, seed_version_before=seed_version_before, drawn=drawn, movement_count=movement_count, booking_in_progress=booking_in_progress, unattributable_flows=unattributable_flows, as_at=as_at, warnings=warnings, payable_check=payable_check)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

