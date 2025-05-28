# TransferAgencyDates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_date** | **datetime** | The date at which the fund is priced, for the order received on ReceivedDate. Can be passed into the request instead of the ReceivedDate to calculate the TransactionDate and ExpectedPaymentDate. | [optional] 
**transaction_date** | **datetime** | The date at which the transaction into or out of the fund is made. | [optional] 
**expected_payment_date** | **datetime** | The date by which the cash is expected to be paid to or from the fund. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.transfer_agency_dates import TransferAgencyDates

# TODO update the JSON string below
json = "{}"
# create an instance of TransferAgencyDates from a JSON string
transfer_agency_dates_instance = TransferAgencyDates.from_json(json)
# print the JSON string representation of the object
print TransferAgencyDates.to_json()

# convert the object into a dict
transfer_agency_dates_dict = transfer_agency_dates_instance.to_dict()
# create an instance of TransferAgencyDates from a dict
transfer_agency_dates_form_dict = transfer_agency_dates.from_dict(transfer_agency_dates_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


