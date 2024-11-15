# TransactionTypeDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope in which the TransactionType was resolved. If the portfolio has a TransactionTypeScope, this will have been used. Otherwise the default scope will have been used. | 
**source** | **str** | The source in which the TransactionType was resolved. | 
**type** | **str** | The resolved TransactionType. More information on TransactionType resolution can be found at https://support.lusid.com/docs/how-does-lusid-resolve-transactions-to-transaction-types | 

## Example

```python
from lusid.models.transaction_type_details import TransactionTypeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTypeDetails from a JSON string
transaction_type_details_instance = TransactionTypeDetails.from_json(json)
# print the JSON string representation of the object
print TransactionTypeDetails.to_json()

# convert the object into a dict
transaction_type_details_dict = transaction_type_details_instance.to_dict()
# create an instance of TransactionTypeDetails from a dict
transaction_type_details_form_dict = transaction_type_details.from_dict(transaction_type_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


