# SetTransactionConfigurationSourceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[SetTransactionConfigurationAlias]**](SetTransactionConfigurationAlias.md) |  | 
**movements** | [**List[TransactionConfigurationMovementDataRequest]**](TransactionConfigurationMovementDataRequest.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 

## Example

```python
from lusid.models.set_transaction_configuration_source_request import SetTransactionConfigurationSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTransactionConfigurationSourceRequest from a JSON string
set_transaction_configuration_source_request_instance = SetTransactionConfigurationSourceRequest.from_json(json)
# print the JSON string representation of the object
print SetTransactionConfigurationSourceRequest.to_json()

# convert the object into a dict
set_transaction_configuration_source_request_dict = set_transaction_configuration_source_request_instance.to_dict()
# create an instance of SetTransactionConfigurationSourceRequest from a dict
set_transaction_configuration_source_request_form_dict = set_transaction_configuration_source_request.from_dict(set_transaction_configuration_source_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


