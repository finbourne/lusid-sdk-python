# TransactionConfigurationTypeAlias


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transaction type | 
**description** | **str** | Brief description of the transaction | 
**transaction_class** | **str** | Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut | 
**transaction_group** | **str** | Group is a set of codes related to a source, or sync. DEPRECATED: This field will be removed, use &#x60;Source&#x60; instead | [optional] 
**source** | **str** | Used to group a set of transaction types | [optional] 
**transaction_roles** | **str** | . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles | 
**is_default** | **bool** | IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source. | [optional] 

## Example

```python
from lusid.models.transaction_configuration_type_alias import TransactionConfigurationTypeAlias

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionConfigurationTypeAlias from a JSON string
transaction_configuration_type_alias_instance = TransactionConfigurationTypeAlias.from_json(json)
# print the JSON string representation of the object
print TransactionConfigurationTypeAlias.to_json()

# convert the object into a dict
transaction_configuration_type_alias_dict = transaction_configuration_type_alias_instance.to_dict()
# create an instance of TransactionConfigurationTypeAlias from a dict
transaction_configuration_type_alias_form_dict = transaction_configuration_type_alias.from_dict(transaction_configuration_type_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


