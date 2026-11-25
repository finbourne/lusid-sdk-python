# FacilityPayableCheck

A Facility's principal balance checked against the facility payable in the Fund's journal, at every date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The outcome. Available values: Agrees (the principal balance equals the payable at every date), Differs (they differ on at least one date, listed in differences, or payable lines name the Facility in another currency, listed in otherCurrencyLines), NotAvailable (the Fund&#39;s journal could not be read; see reason). | 
**payable_accounts** | **List[str]** | The general ledger accounts the Fund&#39;s posting rules mapped the Facility&#39;s principal lines to. | 
**balance** | **float** | The Facility&#39;s principal balance after its last movement, events in Booking status left out. | 
**payable** | **float** | The principal on the facility payable naming the Facility after its last line, the lines of events in Booking status left out. | 
**differences** | [**List[FacilityPayableDifference]**](FacilityPayableDifference.md) | Every date on which the principal balance and the payable differ, each as it stands at the end of that date. | 
**in_flight_lines** | [**List[FacilityPayableLine]**](FacilityPayableLine.md) | The payable lines of events still in Booking status, left out of the comparison as their movements are. | 
**unexplained_lines** | [**List[FacilityPayableLine]**](FacilityPayableLine.md) | Principal lines naming the Facility that no facility event or allocation event booked, such as hand-keyed principal. They are in the comparison, so they show as differences. | 
**unattributed_lines** | [**List[FacilityPayableLine]**](FacilityPayableLine.md) | Principal lines of the Fund that name no Facility, so no Facility&#39;s balance carries them. Listed as breaks; they are not compared. | 
**reason** | **str** | Why the check could not be made, when the status is NotAvailable; or, otherwise, that the Fund&#39;s journal could not be read to the asAt and was read only to the Facility&#39;s last movement, so a payable line after it is not seen. | [optional] 
**other_currency_lines** | [**List[FacilityPayableLine]**](FacilityPayableLine.md) | Principal lines naming the Facility in a currency other than the Facility&#39;s. A Facility is drawn and repaid in its own currency, so they are not converted or compared, and make the status Differs. | 
## Example

```python
from lusid.models.facility_payable_check import FacilityPayableCheck
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: StrictStr = "example_status"
payable_accounts: List[StrictStr] = # Replace with your value
balance: Union[StrictFloat, StrictInt] = # Replace with your value
payable: Union[StrictFloat, StrictInt] = # Replace with your value
differences: List[FacilityPayableDifference] = # Replace with your value
in_flight_lines: List[FacilityPayableLine] = # Replace with your value
unexplained_lines: List[FacilityPayableLine] = # Replace with your value
unattributed_lines: List[FacilityPayableLine] = # Replace with your value
reason: Optional[StrictStr] = "example_reason"
other_currency_lines: List[FacilityPayableLine] = # Replace with your value
facility_payable_check_instance = FacilityPayableCheck(status=status, payable_accounts=payable_accounts, balance=balance, payable=payable, differences=differences, in_flight_lines=in_flight_lines, unexplained_lines=unexplained_lines, unattributed_lines=unattributed_lines, reason=reason, other_currency_lines=other_currency_lines)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

