# TransactionDateWindows


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Transaction Date Window for the left side of a reconciliation | 
**right** | **str** | Transaction Date Window for the right side of a reconciliation | 

## Example

```python
from lusid.models.transaction_date_windows import TransactionDateWindows

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDateWindows from a JSON string
transaction_date_windows_instance = TransactionDateWindows.from_json(json)
# print the JSON string representation of the object
print TransactionDateWindows.to_json()

# convert the object into a dict
transaction_date_windows_dict = transaction_date_windows_instance.to_dict()
# create an instance of TransactionDateWindows from a dict
transaction_date_windows_form_dict = transaction_date_windows.from_dict(transaction_date_windows_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


