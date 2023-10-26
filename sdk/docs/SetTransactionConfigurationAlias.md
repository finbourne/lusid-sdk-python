# SetTransactionConfigurationAlias


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**description** | **str** |  | 
**transaction_class** | **str** |  | 
**transaction_role** | **str** |  | 
**is_default** | **bool** |  | [optional] 

## Example

```python
from lusid.models.set_transaction_configuration_alias import SetTransactionConfigurationAlias

# TODO update the JSON string below
json = "{}"
# create an instance of SetTransactionConfigurationAlias from a JSON string
set_transaction_configuration_alias_instance = SetTransactionConfigurationAlias.from_json(json)
# print the JSON string representation of the object
print SetTransactionConfigurationAlias.to_json()

# convert the object into a dict
set_transaction_configuration_alias_dict = set_transaction_configuration_alias_instance.to_dict()
# create an instance of SetTransactionConfigurationAlias from a dict
set_transaction_configuration_alias_form_dict = set_transaction_configuration_alias.from_dict(set_transaction_configuration_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


