# TransactionConfigurationDataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[TransactionConfigurationTypeAlias]**](TransactionConfigurationTypeAlias.md) | List of transaction codes that map to this specific transaction model | 
**movements** | [**List[TransactionConfigurationMovementDataRequest]**](TransactionConfigurationMovementDataRequest.md) | Movement data for the transaction code | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties attached to the underlying holding. | [optional] 

## Example

```python
from lusid.models.transaction_configuration_data_request import TransactionConfigurationDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionConfigurationDataRequest from a JSON string
transaction_configuration_data_request_instance = TransactionConfigurationDataRequest.from_json(json)
# print the JSON string representation of the object
print TransactionConfigurationDataRequest.to_json()

# convert the object into a dict
transaction_configuration_data_request_dict = transaction_configuration_data_request_instance.to_dict()
# create an instance of TransactionConfigurationDataRequest from a dict
transaction_configuration_data_request_form_dict = transaction_configuration_data_request.from_dict(transaction_configuration_data_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


