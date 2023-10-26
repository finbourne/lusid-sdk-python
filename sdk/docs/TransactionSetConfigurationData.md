# TransactionSetConfigurationData

A collection of the data required to configure transaction types..

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_configs** | [**List[TransactionConfigurationData]**](TransactionConfigurationData.md) | Collection of transaction type models | 
**side_definitions** | [**List[SideConfigurationData]**](SideConfigurationData.md) | Collection of side definitions | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.transaction_set_configuration_data import TransactionSetConfigurationData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSetConfigurationData from a JSON string
transaction_set_configuration_data_instance = TransactionSetConfigurationData.from_json(json)
# print the JSON string representation of the object
print TransactionSetConfigurationData.to_json()

# convert the object into a dict
transaction_set_configuration_data_dict = transaction_set_configuration_data_instance.to_dict()
# create an instance of TransactionSetConfigurationData from a dict
transaction_set_configuration_data_form_dict = transaction_set_configuration_data.from_dict(transaction_set_configuration_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


