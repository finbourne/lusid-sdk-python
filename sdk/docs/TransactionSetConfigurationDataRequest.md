# TransactionSetConfigurationDataRequest

A bundle of requests to configure a set of transaction types.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_config_requests** | [**List[TransactionConfigurationDataRequest]**](TransactionConfigurationDataRequest.md) | Collection of transaction type models | 
**side_config_requests** | [**List[SideConfigurationDataRequest]**](SideConfigurationDataRequest.md) | Collection of side definition requests. | [optional] 

## Example

```python
from lusid.models.transaction_set_configuration_data_request import TransactionSetConfigurationDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSetConfigurationDataRequest from a JSON string
transaction_set_configuration_data_request_instance = TransactionSetConfigurationDataRequest.from_json(json)
# print the JSON string representation of the object
print TransactionSetConfigurationDataRequest.to_json()

# convert the object into a dict
transaction_set_configuration_data_request_dict = transaction_set_configuration_data_request_instance.to_dict()
# create an instance of TransactionSetConfigurationDataRequest from a dict
transaction_set_configuration_data_request_form_dict = transaction_set_configuration_data_request.from_dict(transaction_set_configuration_data_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


