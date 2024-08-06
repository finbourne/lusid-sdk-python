# TransactionPrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**type** | **str** | The available values are: Price, Yield, Spread, CashFlowPerUnit | [optional] 

## Example

```python
from lusid.models.transaction_price import TransactionPrice

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPrice from a JSON string
transaction_price_instance = TransactionPrice.from_json(json)
# print the JSON string representation of the object
print TransactionPrice.to_json()

# convert the object into a dict
transaction_price_dict = transaction_price_instance.to_dict()
# create an instance of TransactionPrice from a dict
transaction_price_form_dict = transaction_price.from_dict(transaction_price_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


