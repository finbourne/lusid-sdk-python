# TransactionTypeAlias


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transaction type | 
**description** | **str** | Brief description of the transaction | 
**transaction_class** | **str** | Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut | 
**transaction_roles** | **str** | Transactions role within a class. E.g. Increase a long position | 
**is_default** | **bool** | IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source. | [optional] 

## Example

```python
from lusid.models.transaction_type_alias import TransactionTypeAlias

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTypeAlias from a JSON string
transaction_type_alias_instance = TransactionTypeAlias.from_json(json)
# print the JSON string representation of the object
print TransactionTypeAlias.to_json()

# convert the object into a dict
transaction_type_alias_dict = transaction_type_alias_instance.to_dict()
# create an instance of TransactionTypeAlias from a dict
transaction_type_alias_form_dict = transaction_type_alias.from_dict(transaction_type_alias_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


