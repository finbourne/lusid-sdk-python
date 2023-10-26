# TransactionConfigurationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[TransactionConfigurationTypeAlias]**](TransactionConfigurationTypeAlias.md) | List of transaction types that map to this specific transaction configuration | 
**movements** | [**List[TransactionConfigurationMovementData]**](TransactionConfigurationMovementData.md) | Movement data for the transaction type | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties attached to the transaction type | [optional] 

## Example

```python
from lusid.models.transaction_configuration_data import TransactionConfigurationData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionConfigurationData from a JSON string
transaction_configuration_data_instance = TransactionConfigurationData.from_json(json)
# print the JSON string representation of the object
print TransactionConfigurationData.to_json()

# convert the object into a dict
transaction_configuration_data_dict = transaction_configuration_data_instance.to_dict()
# create an instance of TransactionConfigurationData from a dict
transaction_configuration_data_form_dict = transaction_configuration_data.from_dict(transaction_configuration_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


