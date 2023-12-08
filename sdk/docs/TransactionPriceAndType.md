# TransactionPriceAndType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from lusid.models.transaction_price_and_type import TransactionPriceAndType

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPriceAndType from a JSON string
transaction_price_and_type_instance = TransactionPriceAndType.from_json(json)
# print the JSON string representation of the object
print TransactionPriceAndType.to_json()

# convert the object into a dict
transaction_price_and_type_dict = transaction_price_and_type_instance.to_dict()
# create an instance of TransactionPriceAndType from a dict
transaction_price_and_type_form_dict = transaction_price_and_type.from_dict(transaction_price_and_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


