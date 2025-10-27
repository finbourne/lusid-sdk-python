# TransferAgencyDates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_date** | **datetime** | The date at which the fund is priced, for the order received on ReceivedDate. Can be passed into the request instead of the ReceivedDate to calculate the TransactionDate and ExpectedPaymentDate. If both the received date and price date are given, a failure is returned. | [optional] 
**transaction_date** | **datetime** | The date at which the transaction into or out of the fund is made. | [optional] 
**expected_payment_date** | **datetime** | The date by which the cash is expected to be paid to or from the fund. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transfer_agency_dates import TransferAgencyDates
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

price_date: Optional[datetime] = # Replace with your value
transaction_date: Optional[datetime] = # Replace with your value
expected_payment_date: Optional[datetime] = # Replace with your value
links: Optional[List[Link]] = None
transfer_agency_dates_instance = TransferAgencyDates(price_date=price_date, transaction_date=transaction_date, expected_payment_date=expected_payment_date, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

